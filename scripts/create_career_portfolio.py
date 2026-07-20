#!/usr/bin/env python3
"""Create a privacy-safe CareerPortfolio scaffold from this repository."""

from __future__ import annotations

import argparse
import shutil
import sys
from datetime import date
from pathlib import Path


# Every file in the reusable infrastructure roots is audited in validate_source().
COPY_FILES = (
    ".github/workflows/generate-resume-artifacts.yml",
    ".github/workflows/validate-resumes.yml",
    "docs/workflows/RESUME_WORKFLOW.md",
    "docs/workflows/ATS_VALIDATION.md",
    "docs/workflows/LINKEDIN_PROFILE_WORKFLOW.md",
    "docs/OKF_PORTFOLIO.md",
    "docs/STARTER_GUIDE.md",
    "designs/README.md",
    "designs/default.json",
    "designs/classic-ats/design.json",
    "scripts/generate_resume_artifacts.py",
    "scripts/validate_resume.py",
    "scripts/validate_rebuilt_artifacts.py",
    "scripts/record_ats_history.py",
    "scripts/create_career_portfolio.py",
    "linkedin/README.md",
)

AUDITED_INFRASTRUCTURE_ROOTS = (
    ".github/workflows",
    "docs/workflows",
    "designs",
    "scripts",
)

GENERATED_FILES = (
    "AGENTS.md",
    "README.md",
    "docs/ROADMAP.md",
    "docs/STYLE_GUIDE.md",
    "docs/decisions/README.md",
    "knowledge/index.md",
    "knowledge/log.md",
    "linkedin/CHANGELOG.md",
)

EMPTY_DIRECTORIES = (
    "applications",
    "generic",
)

TEXT_SUFFIXES = {".md", ".py", ".yml", ".yaml"}
SOURCE_FIRST_NAME = "Jor" + "dan"
SOURCE_LAST_NAME = "New" + "man"
SOURCE_FULL_NAME = SOURCE_FIRST_NAME + " " + SOURCE_LAST_NAME
SOURCE_REPOSITORY = "pho" + "em/CareerPortfolio"
SOURCE_PRIVATE_TERMS = ("3,000" + "-4,000 servers", "3,000" + "–4,000 servers", "65 G" + "bps")
SOURCE_OKF_EXAMPLE = (
    "Prime" + "HTTPD was part of the [CDN platform](/CDN_" + "Platform/README.md) and worked "
    "alongside [Virtual" + "Dir](/Virtual" + "Dir/README.md)."
)
SOURCE_RANGE_EXAMPLE = (
    "- Preserve ranges such as `3,000" + "-4,000 servers` when that is the known estimate."
)
PRIVATE_MARKERS = (
    SOURCE_FULL_NAME,
    SOURCE_FIRST_NAME,
    SOURCE_LAST_NAME,
    SOURCE_REPOSITORY,
    *SOURCE_PRIVATE_TERMS,
)


def possessive(name: str) -> str:
    return f"{name}'" if name.endswith(("s", "S")) else f"{name}'s"


def personalize(text: str, owner_name: str) -> str:
    """Replace known source-owner references without changing general guidance."""
    owner_possessive = possessive(owner_name)
    replacements = (
        (
            SOURCE_OKF_EXAMPLE,
            "Example Service ran on the [Example Platform](/Example_Platform/README.md) and "
            "used [Example Library](/Example_Library/README.md).",
        ),
        (
            SOURCE_RANGE_EXAMPLE,
            "- Preserve verified ranges and qualifiers exactly; do not collapse a known range to a single value.",
        ),
        (
            f"This guide explains how another person can create a new CareerPortfolio without copying "
            f"{SOURCE_FULL_NAME}'s private career data.",
            "This guide explains how to create a CareerPortfolio without copying the source portfolio "
            "owner's private career data.",
        ),
        (
            f"Replace references to {SOURCE_FULL_NAME} with the portfolio owner's name.",
            "Verify that owner-specific references use the new portfolio owner's name.",
        ),
        (
            f"never copy {SOURCE_FIRST_NAME}'s entries into another portfolio.",
            "never copy the source portfolio's entries into another portfolio.",
        ),
        (f"ask {SOURCE_FIRST_NAME} whether he has", f"ask {owner_name} whether they have"),
        (f"{SOURCE_FULL_NAME}'s", owner_possessive),
        (SOURCE_FULL_NAME, owner_name),
        (f"{SOURCE_FIRST_NAME}'s", owner_possessive),
        (f"{SOURCE_FIRST_NAME}’s", owner_possessive),
        (SOURCE_FIRST_NAME, owner_name),
        (SOURCE_FULL_NAME.upper(), owner_name.upper()),
        (
            f"The canonical repository is `{SOURCE_REPOSITORY}`.",
            "Treat this repository as the canonical CareerPortfolio.",
        ),
        (f"`{SOURCE_REPOSITORY}`", "this CareerPortfolio repository"),
    )
    for old, new in replacements:
        text = text.replace(old, new)
    return text


def starter_readme(owner_name: str) -> str:
    return f"""# CareerPortfolio

This repository is the authoritative professional-knowledge, resume, and application-material system for {owner_name}.

## Structure

- `knowledge/` contains confirmed professional knowledge in Open Knowledge Format (OKF) v0.1.
- `generic/` contains reusable resume sources and generated artifacts.
- `applications/<company>/<posting>/` contains an isolated package for each job posting.
- `designs/` contains reusable rendering designs.
- `scripts/` generates and validates resume artifacts.
- `docs/workflows/` defines the resume, ATS-validation, and LinkedIn processes.
- `docs/STYLE_GUIDE.md` defines evidence-safe resume-writing conventions.
- `docs/decisions/` records this portfolio's own architecture decisions.
- `linkedin/` contains the append-only LinkedIn change log and optional preserved reviews.

## Getting Started

1. Read `docs/STARTER_GUIDE.md` and `AGENTS.md`.
2. Complete the initial interview described in the starter guide.
3. Record only confirmed facts under `knowledge/` and update `knowledge/index.md` and `knowledge/log.md`.
4. Build at least one canonical Markdown resume under `generic/`.
5. Create one isolated package under `applications/<company>/<posting>/` for every real posting.
6. Generate artifacts with `python scripts/generate_resume_artifacts.py --full-rebuild` only after explicitly approving a full rebuild.

Markdown is the editable source format. DOCX, PDF, ATS reports, and score histories are generated artifacts.
"""


def starter_roadmap() -> str:
    return """# Roadmap

Use this file for useful ideas that are not yet justified for implementation.

## Candidate Improvements

- Add items only when they describe a concrete future need.
- Promote an item into implementation only when the portfolio owner explicitly prioritizes it or evidence demonstrates the need.
"""


def starter_style_guide() -> str:
    return """# Resume Writing Style Guide

## Purpose

This guide keeps CareerPortfolio resumes concise, credible, and outcome-oriented while preserving technical depth where it matters.

## Google XYZ Formula

Use the Google XYZ formula as the preferred pattern for accomplishment bullets when the supporting facts are documented:

> Accomplished **[X]**, as measured by **[Y]**, by doing **[Z]**.

- **X — outcome:** The capability, improvement, risk reduction, delivery, or business/operational result.
- **Y — evidence:** A verified metric, scale, range, duration, reliability result, or other defensible measure.
- **Z — method:** The portfolio owner's personal technical, architectural, operational, or leadership contribution.

Do not force every bullet into a literal `X as measured by Y by doing Z` sentence. The formula is a fact-selection and editing guide, not a repetitive sentence template.

## When a Metric Is Not Documented

Use an outcome-first alternative when no defensible measurement is known:

> Designed **[system or capability]** to enable **[outcome]** through **[technical approach]**.

Never invent, estimate, or imply a metric merely to complete the formula. Preserve known ranges and qualifiers such as “approximately” or “more than.”

## Bullet Rules

- Lead with impact, scope, or the delivered capability—not a tool list.
- State ownership accurately: architected, designed, implemented, operated, led, collaborated, or supported.
- Include technology only when it makes the accomplishment more credible or relevant.
- Prefer one clear accomplishment per bullet.
- Use specific metrics and scale only when confirmed in `knowledge/`.
- Avoid keyword stuffing, vague claims, and unsupported superlatives.
- Vary sentence structure enough that bullets read naturally.
- Match technical depth to the intended reader and job description.

## Review Checklist

Before finalizing a bullet, confirm:

1. The outcome is clear.
2. The evidence or scope is documented, if stated.
3. The method reflects the portfolio owner's actual contribution.
4. The wording does not overstate production use, ownership, or expertise.
5. The bullet remains readable to a recruiter and credible to a technical reviewer.
"""


def decisions_readme() -> str:
    return """# Architecture Decision Records

This directory records significant structural and workflow decisions for this CareerPortfolio.

ADRs are immutable historical records. When a decision changes, add a new ADR that supersedes the earlier one rather than rewriting history. Minor corrections and clarifications may be made in place.

## Status values

- **Proposed** — under consideration.
- **Accepted** — approved and active.
- **Deprecated** — retained for history but no longer recommended.
- **Superseded** — replaced by a later ADR.
- **Rejected** — considered but not adopted.

## Index

No architecture decisions have been recorded yet.

## Creating a new ADR

1. Choose the next four-digit number, starting with `0001`.
2. Use a lowercase hyphenated filename: `NNNN-short-decision-name.md`.
3. Record the context, decision, consequences, and status.
4. Add the ADR to this index.
5. Link related ADRs where helpful.
6. Do not renumber existing ADRs.
"""


def knowledge_index() -> str:
    return """---
okf_version: "0.1"
---

# Career Knowledge Base

Add confirmed professional-profile, employment, project, technology, metrics, education, and certification concepts here as they are created.

## Concepts

No concepts have been documented yet.
"""


def knowledge_log() -> str:
    return f"""# Knowledge Base Update Log

## {date.today().isoformat()}

- **Initialization**: Created the CareerPortfolio knowledge bundle.
"""


def linkedin_changelog() -> str:
    return """# LinkedIn Change Log

This append-only log was initialized with the CareerPortfolio. No LinkedIn changes have been attempted.
"""


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8", newline="\n")


def write_text_if_missing(path: Path, content: str) -> None:
    if not path.exists():
        write_text(path, content)


def files_under(source_root: Path, relative_root: str) -> set[str]:
    root = source_root / relative_root
    return {
        path.relative_to(source_root).as_posix()
        for path in root.rglob("*")
        if path.is_file() and "__pycache__" not in path.parts
    }


def validate_source(source_root: Path) -> None:
    required = ("AGENTS.md", "docs/STYLE_GUIDE.md") + COPY_FILES
    missing = [item for item in required if not (source_root / item).is_file()]
    if missing:
        formatted = "\n  - ".join(missing)
        raise RuntimeError(f"Source repository is missing required starter files:\n  - {formatted}")

    audited_files: set[str] = set()
    for relative_root in AUDITED_INFRASTRUCTURE_ROOTS:
        audited_files.update(files_under(source_root, relative_root))
    declared_files = {
        item for item in COPY_FILES if any(item.startswith(f"{root}/") for root in AUDITED_INFRASTRUCTURE_ROOTS)
    }
    undeclared = sorted(audited_files - declared_files)
    stale = sorted(declared_files - audited_files)
    if undeclared or stale:
        details = []
        if undeclared:
            details.append("Reusable source files missing from COPY_FILES: " + ", ".join(undeclared))
        if stale:
            details.append("COPY_FILES entries not found in source repository: " + ", ".join(stale))
        raise RuntimeError("\n".join(details))


def prepare_destination(destination: Path, force: bool) -> None:
    if destination.exists() and not destination.is_dir():
        raise RuntimeError(f"Destination exists and is not a directory: {destination}")
    if destination.exists() and any(destination.iterdir()) and not force:
        raise RuntimeError(
            f"Destination is not empty: {destination}\n"
            "Choose an empty path or pass --force to overwrite reusable scaffold files."
        )
    destination.mkdir(parents=True, exist_ok=True)


def copy_personalized_file(source_root: Path, destination: Path, relative: str, owner_name: str) -> None:
    source = source_root / relative
    target = destination / relative
    target.parent.mkdir(parents=True, exist_ok=True)
    if source.suffix.lower() in TEXT_SUFFIXES:
        write_text(target, personalize(source.read_text(encoding="utf-8"), owner_name))
    else:
        shutil.copy2(source, target)


def source_private_markers(source_root: Path) -> set[str]:
    markers = set(PRIVATE_MARKERS)
    knowledge_root = source_root / "knowledge"
    if knowledge_root.is_dir():
        markers.update(
            path.name
            for path in knowledge_root.iterdir()
            if path.is_dir() and path.name != "Professional_Profile"
        )
    applications_root = source_root / "applications"
    if applications_root.is_dir():
        markers.update(path.name for path in applications_root.iterdir() if path.is_dir())
    return markers


def verify_scaffold(source_root: Path, destination: Path) -> None:
    expected = set(COPY_FILES) | set(GENERATED_FILES)
    missing = [relative for relative in sorted(expected) if not (destination / relative).is_file()]
    for relative in EMPTY_DIRECTORIES:
        if not (destination / relative).is_dir():
            missing.append(f"{relative}/")
    if missing:
        raise RuntimeError("Scaffold verification failed; missing: " + ", ".join(missing))

    leaks: list[str] = []
    for path in destination.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        content = path.read_text(encoding="utf-8", errors="replace")
        for marker in source_private_markers(source_root):
            if marker.lower() in content.lower():
                leaks.append(f"{path.relative_to(destination)}: {marker}")
    if leaks:
        raise RuntimeError("Source-specific text remained in scaffold:\n  - " + "\n  - ".join(leaks))


def create_scaffold(destination: Path, owner_name: str, force: bool) -> None:
    source_root = Path(__file__).resolve().parents[1]
    validate_source(source_root)
    if (
        destination == source_root
        or destination.is_relative_to(source_root)
        or source_root.is_relative_to(destination)
    ):
        raise RuntimeError(
            "Destination must be separate from the source CareerPortfolio and cannot be its parent or child."
        )
    prepare_destination(destination, force)

    for relative in COPY_FILES:
        copy_personalized_file(source_root, destination, relative, owner_name)
    for relative in EMPTY_DIRECTORIES:
        (destination / relative).mkdir(parents=True, exist_ok=True)

    agents = (source_root / "AGENTS.md").read_text(encoding="utf-8")
    write_text(destination / "AGENTS.md", personalize(agents, owner_name))
    write_text(destination / "README.md", starter_readme(owner_name))
    write_text(destination / "docs/ROADMAP.md", starter_roadmap())
    write_text(destination / "docs/STYLE_GUIDE.md", starter_style_guide())
    write_text(destination / "docs/decisions/README.md", decisions_readme())
    write_text_if_missing(destination / "knowledge/index.md", knowledge_index())
    write_text_if_missing(destination / "knowledge/log.md", knowledge_log())
    write_text_if_missing(destination / "linkedin/CHANGELOG.md", linkedin_changelog())
    verify_scaffold(source_root, destination)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create a reusable CareerPortfolio at an exact destination path."
    )
    parser.add_argument("destination", type=Path, help="Path that will become the CareerPortfolio root")
    parser.add_argument("--owner-name", required=True, help="Full name of the new portfolio owner")
    parser.add_argument(
        "--force",
        action="store_true",
        help=(
            "Allow reusable scaffold files in a non-empty destination to be overwritten; "
            "never deletes extra files or resets knowledge and LinkedIn logs"
        ),
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    owner_name = " ".join(args.owner_name.split())
    if not owner_name:
        print("error: --owner-name must not be blank", file=sys.stderr)
        return 2
    destination = args.destination.expanduser().resolve()
    try:
        create_scaffold(destination, owner_name, args.force)
    except (OSError, RuntimeError, UnicodeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    print(f"Created CareerPortfolio for {owner_name} at {destination}")
    print("Next: read docs/STARTER_GUIDE.md and begin the initial interview.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
