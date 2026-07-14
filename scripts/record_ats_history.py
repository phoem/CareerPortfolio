#!/usr/bin/env python3
"""Append one deduplicated ATS validation result to a Markdown history file."""
from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--result", type=Path, required=True)
    parser.add_argument("--history", type=Path, required=True)
    args = parser.parse_args()

    result = json.loads(args.result.read_text(encoding="utf-8"))
    hashes = result.get("hashes", {})
    artifact_key = result.get("validator_version", "") + "".join(
        hashes.get(name, "") for name in ("resume", "docx", "pdf", "job")
    )
    marker = hashlib.sha256(artifact_key.encode("ascii")).hexdigest()

    existing = (
        args.history.read_text(encoding="utf-8")
        if args.history.exists()
        else "# ATS Validation History\n"
    )
    if marker in existing:
        print("History already contains this artifact set.")
        return 0

    categories = result.get("categories", {})
    category_summary = "; ".join(
        f"{name}: {details.get('score', 0)}" for name, details in categories.items()
    )
    score_type = "Targeted readiness" if "job" in hashes else "Generic baseline"
    timestamp = datetime.now(timezone.utc).isoformat(timespec="seconds")
    entry = (
        f"\n\n## {timestamp} — {result['overall_score']}/100 "
        f"({result['disposition']})\n\n"
        f"- **Score type:** {score_type}\n"
        f"- **Validator:** v{result['validator_version']}\n"
        f"- **Revision pass:** {result.get('pass_number', 0)} of 3\n"
        f"- **Categories:** {category_summary}\n"
        f"- **Artifact set:** `{marker}`\n"
    )
    args.history.parent.mkdir(parents=True, exist_ok=True)
    args.history.write_text(existing.rstrip() + entry + "\n", encoding="utf-8")
    print(f"Recorded {result['overall_score']}/100 in {args.history}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
