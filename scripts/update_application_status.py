#!/usr/bin/env python3
"""Validate application status records and refresh the master status index."""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from datetime import date, datetime
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
APPLICATIONS_ROOT = ROOT / "applications"
MASTER_PATH = APPLICATIONS_ROOT / "STATUS.json"
STATUS_FILENAME = "APPLICATION_STATUS.json"
SCHEMA_VERSION = 1

STATUSES = (
    "unknown",
    "not_applied",
    "applied",
    "interviewing",
    "offer_received",
    "closed",
)
OUTCOMES = (
    "not_selected",
    "withdrawn",
    "offer_declined",
    "accepted",
)
STATUS_FIELDS = {"schema_version", "status", "outcome", "history", "note"}
HISTORY_FIELDS = {"status", "outcome", "occurred_at", "recorded_at", "source", "note"}


def load_json(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("top-level JSON value must be an object")
    return data


def valid_iso_date_or_datetime(value: object) -> bool:
    if not isinstance(value, str) or not value.strip():
        return False
    try:
        if "T" in value:
            datetime.fromisoformat(value.replace("Z", "+00:00"))
        else:
            date.fromisoformat(value)
    except ValueError:
        return False
    return True


def validate_state(
    record: dict[str, Any],
    *,
    label: str,
    allowed_fields: set[str],
    require_schema: bool,
) -> list[str]:
    errors: list[str] = []
    unknown_fields = sorted(set(record) - allowed_fields)
    if unknown_fields:
        errors.append(f"{label}: unknown field(s): {', '.join(unknown_fields)}")

    if require_schema and record.get("schema_version") != SCHEMA_VERSION:
        errors.append(f"{label}: schema_version must be {SCHEMA_VERSION}")

    status = record.get("status")
    if status not in STATUSES:
        errors.append(f"{label}: status must be one of {', '.join(STATUSES)}")

    outcome = record.get("outcome")
    if outcome is not None and outcome not in OUTCOMES:
        errors.append(f"{label}: outcome must be one of {', '.join(OUTCOMES)}")
    if outcome is not None and status != "closed":
        errors.append(f"{label}: outcome is allowed only when status is closed")

    note = record.get("note")
    if note is not None and (not isinstance(note, str) or not note.strip()):
        errors.append(f"{label}: note must be a non-empty string when present")
    return errors


def validate_status(path: Path, record: dict[str, Any]) -> list[str]:
    relative = path.relative_to(ROOT).as_posix()
    errors = validate_state(
        record,
        label=relative,
        allowed_fields=STATUS_FIELDS,
        require_schema=True,
    )

    history = record.get("history")
    if history is not None and not isinstance(history, list):
        errors.append(f"{relative}: history must be an array when present")
        return errors

    if isinstance(history, list):
        for index, event in enumerate(history):
            label = f"{relative}: history[{index}]"
            if not isinstance(event, dict):
                errors.append(f"{label} must be an object")
                continue
            errors.extend(
                validate_state(
                    event,
                    label=label,
                    allowed_fields=HISTORY_FIELDS,
                    require_schema=False,
                )
            )
            if not valid_iso_date_or_datetime(event.get("recorded_at")):
                errors.append(f"{label}: recorded_at must be an ISO date or datetime")
            if "occurred_at" in event and not valid_iso_date_or_datetime(event.get("occurred_at")):
                errors.append(f"{label}: occurred_at must be an ISO date or datetime when present")
            source = event.get("source")
            if not isinstance(source, str) or not source.strip():
                errors.append(f"{label}: source must be a non-empty string")

        if history:
            latest = history[-1]
            if isinstance(latest, dict):
                if latest.get("status") != record.get("status"):
                    errors.append(f"{relative}: current status must match the last history event")
                if latest.get("outcome") != record.get("outcome"):
                    errors.append(f"{relative}: current outcome must match the last history event")

    return errors


def build_master() -> tuple[dict[str, Any], list[str]]:
    errors: list[str] = []
    applications: list[dict[str, Any]] = []
    manifest_paths = sorted(APPLICATIONS_ROOT.glob("**/APPLICATION.json"))
    manifest_directories = {path.parent.resolve() for path in manifest_paths}

    for orphan in sorted(APPLICATIONS_ROOT.glob(f"**/{STATUS_FILENAME}")):
        if orphan.parent.resolve() not in manifest_directories:
            errors.append(
                f"{orphan.relative_to(ROOT).as_posix()}: status file has no sibling APPLICATION.json"
            )

    for manifest_path in manifest_paths:
        package = manifest_path.parent
        status_path = package / STATUS_FILENAME
        relative_package = package.relative_to(ROOT).as_posix()
        if not status_path.is_file():
            errors.append(f"{relative_package}: missing {STATUS_FILENAME}")
            continue

        try:
            manifest = load_json(manifest_path)
        except (OSError, UnicodeError, json.JSONDecodeError, ValueError) as exc:
            errors.append(f"{manifest_path.relative_to(ROOT).as_posix()}: {exc}")
            continue
        try:
            status_record = load_json(status_path)
        except (OSError, UnicodeError, json.JSONDecodeError, ValueError) as exc:
            errors.append(f"{status_path.relative_to(ROOT).as_posix()}: {exc}")
            continue

        errors.extend(validate_status(status_path, status_record))
        for required in ("company", "role"):
            value = manifest.get(required)
            if not isinstance(value, str) or not value.strip():
                errors.append(
                    f"{manifest_path.relative_to(ROOT).as_posix()}: {required} must be a non-empty string"
                )

        item: dict[str, Any] = {
            "company": manifest.get("company"),
            "role": manifest.get("role"),
        }
        requisition = manifest.get("requisition_id")
        if requisition:
            item["requisition_id"] = str(requisition)
        item["package"] = relative_package
        item["status"] = status_record.get("status")
        if status_record.get("outcome") is not None:
            item["outcome"] = status_record["outcome"]
        applications.append(item)

    applications.sort(
        key=lambda item: (
            str(item.get("company", "")).casefold(),
            str(item.get("role", "")).casefold(),
            str(item.get("package", "")),
        )
    )
    status_counts = Counter(item.get("status") for item in applications)
    outcome_counts = Counter(item.get("outcome") for item in applications if item.get("outcome"))
    master: dict[str, Any] = {
        "schema_version": SCHEMA_VERSION,
        "generated_from": f"applications/**/{STATUS_FILENAME}",
        "summary": {
            "total": len(applications),
            "by_status": {status: status_counts[status] for status in STATUSES if status_counts[status]},
            "by_outcome": {
                outcome: outcome_counts[outcome] for outcome in OUTCOMES if outcome_counts[outcome]
            },
        },
        "applications": applications,
    }
    return master, errors


def serialized(payload: dict[str, Any]) -> str:
    return json.dumps(payload, indent=2, ensure_ascii=False) + "\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate application statuses and update applications/STATUS.json."
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Validate status records and fail if the master index is stale; do not write files.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    master, errors = build_master()
    expected = serialized(master)

    if errors:
        for error in errors:
            print(f"error: {error}", file=sys.stderr)
        return 1

    if args.check:
        if not MASTER_PATH.is_file():
            print(f"error: {MASTER_PATH.relative_to(ROOT).as_posix()} is missing", file=sys.stderr)
            return 1
        actual = MASTER_PATH.read_text(encoding="utf-8")
        if actual != expected:
            print(
                "error: applications/STATUS.json is stale; run "
                "python scripts/update_application_status.py",
                file=sys.stderr,
            )
            return 1
        print(f"Validated {len(master['applications'])} application status record(s).")
        return 0

    MASTER_PATH.write_text(expected, encoding="utf-8", newline="\n")
    print(f"Updated {MASTER_PATH.relative_to(ROOT).as_posix()} with {len(master['applications'])} record(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
