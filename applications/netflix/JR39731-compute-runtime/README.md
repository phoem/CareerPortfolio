# Netflix JR39731 — Compute Runtime

This directory contains one application package for Netflix requisition `JR39731`, Distributed Systems Engineer (L5 + L6), Compute Runtime.

Each distinct Netflix posting receives its own sibling directory under `applications/netflix/`. Job descriptions are never combined into or overwritten inside a single company-level file.

## Package contents

- `APPLICATION.json` — machine-readable package manifest.
- `JOB_DESCRIPTION.md` — exact job posting text when available.
- resume and cover-letter Markdown sources plus generated DOCX/PDF files.
- `DESIGN.json` — persistent design override for every future rebuild of this application.
- `DESIGN_NEXT.json` — optional one-build override; it takes precedence and is removed after successful generation.
- `validation/` — ATS report, result data, and score history.

The exact posting still needs to be restored as `JOB_DESCRIPTION.md` before targeted ATS validation can run.
