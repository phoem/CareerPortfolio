#!/usr/bin/env python3
"""Validate only resume artifacts listed by the immediately preceding build."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run(*arguments: str) -> None:
    subprocess.run([sys.executable, *arguments], cwd=ROOT, check=True)


def application_manifest_for(source: Path) -> Path | None:
    for parent in (source.parent, *source.parents):
        manifest = parent / "APPLICATION.json"
        if manifest.exists():
            return manifest
        if parent == ROOT:
            break
    return None


def validation_paths(source: Path, manifest: dict | None) -> tuple[Path, Path, Path]:
    if manifest is None:
        directory = ROOT / "generic" / "validation"
        prefix = f"{source.stem}-ATS"
        return (
            directory / f"{prefix}_REPORT.md",
            directory / f"{prefix}_RESULT.json",
            directory / f"{prefix}_HISTORY.md",
        )

    directory = source.parent / "validation"
    resume_count = sum(1 for item in manifest.get("artifacts", []) if item.get("type") == "resume")
    prefix = "ATS" if resume_count == 1 else f"{source.stem}-ATS"
    return (
        directory / f"{prefix}_REPORT.md",
        directory / f"{prefix}_RESULT.json",
        directory / f"{prefix}_HISTORY.md",
    )


def write_pending(report: Path, job_filename: str) -> None:
    report.parent.mkdir(parents=True, exist_ok=True)
    report.write_text(
        "# ATS Readiness Report\n\n"
        "Targeted validation is pending because the exact job posting has not yet "
        f"been stored as `{job_filename}` in this application package.\n\n"
        "The validator will not reconstruct qualifications from the tailored resume "
        "or from memory. Add the exact posting, rebuild the resume, and validation "
        "will run for that rebuilt artifact.\n",
        encoding="utf-8",
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", required=True, type=Path)
    args = parser.parse_args()
    payload = json.loads(args.manifest.read_text(encoding="utf-8"))

    validated = 0
    for item in payload.get("rebuilt", []):
        if item.get("artifact_type") != "resume":
            continue

        source = ROOT / item["source"]
        docx = ROOT / item["docx"]
        pdf = ROOT / item["pdf"]
        application_path = application_manifest_for(source)
        application = json.loads(application_path.read_text(encoding="utf-8")) if application_path else None
        report, result, history = validation_paths(source, application)
        report.parent.mkdir(parents=True, exist_ok=True)

        command = [
            "scripts/validate_resume.py",
            "--resume",
            str(source.relative_to(ROOT)),
            "--docx",
            str(docx.relative_to(ROOT)),
            "--pdf",
            str(pdf.relative_to(ROOT)),
        ]
        if application is not None:
            job_filename = str(application.get("job_description", "JOB_DESCRIPTION.md"))
            job = application_path.parent / job_filename
            if not job.exists():
                write_pending(report, job_filename)
                print(f"Validation pending for {source.relative_to(ROOT)}: missing {job_filename}")
                continue
            command.extend(["--job", str(job.relative_to(ROOT))])

        command.extend(
            [
                "--output",
                str(report.relative_to(ROOT)),
                "--json-output",
                str(result.relative_to(ROOT)),
            ]
        )
        run(*command)
        run(
            "scripts/record_ats_history.py",
            "--result",
            str(result.relative_to(ROOT)),
            "--history",
            str(history.relative_to(ROOT)),
        )
        validated += 1
        print(f"Validated rebuilt resume {source.relative_to(ROOT)}")

    print(f"Validated {validated} rebuilt resume(s).")


if __name__ == "__main__":
    main()
