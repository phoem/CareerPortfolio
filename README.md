# Jordan Newman Resume Package

This repository stores three canonical generic resumes, targeted application packages, and an incremental project-knowledge portfolio used to create accurate role-specific resumes and cover letters.

## Canonical Generic Resumes

| Document | Markdown | DOCX | PDF |
|---|---:|---:|---:|
| Senior Software Engineer | `generic/Jordan_Newman_Generic_Senior_Software_Engineer_Resume.md` | `generic/Jordan_Newman_Generic_Senior_Software_Engineer_Resume.docx` | `generic/Jordan_Newman_Generic_Senior_Software_Engineer_Resume.pdf` |
| Software Architect | `generic/Jordan_Newman_Generic_Software_Architect_Resume.md` | `generic/Jordan_Newman_Generic_Software_Architect_Resume.docx` | `generic/Jordan_Newman_Generic_Software_Architect_Resume.pdf` |
| Backend / Infrastructure | `generic/Jordan_Newman_Generic_Backend_Infrastructure_Resume.md` | `generic/Jordan_Newman_Generic_Backend_Infrastructure_Resume.docx` | `generic/Jordan_Newman_Generic_Backend_Infrastructure_Resume.pdf` |

## Targeted Packages

### Netflix - Distributed Systems Engineer, Compute Runtime

| Document | Markdown | Generated DOCX | Generated PDF |
|---|---:|---:|---:|
| Resume | `netflix/Jordan_Newman_Netflix_Compute_Runtime_Resume.md` | `netflix/Jordan_Newman_Netflix_Compute_Runtime_Resume.docx` | `netflix/Jordan_Newman_Netflix_Compute_Runtime_Resume.pdf` |
| Cover Letter | `netflix/Jordan_Newman_Netflix_Compute_Runtime_Cover_Letter.md` | `netflix/Jordan_Newman_Netflix_Compute_Runtime_Cover_Letter.docx` | `netflix/Jordan_Newman_Netflix_Compute_Runtime_Cover_Letter.pdf` |

### Starlink

The existing Starlink ATS resume, recruiter resume, and cover letter remain under `starlink/`.

## Project Portfolio

The `portfolio/` directory is the factual source of truth for project descriptions used across resumes and interview preparation. It is intentionally incremental: confirmed information is recorded, unknown details are omitted or listed as open questions, and new project knowledge is added only as it becomes relevant.

Current entries include PrimeHTTPD, the CDN platform, VirtualDir, PrimeDump, PrimeDNSTop, KeepClean, StatCache, TAFOS, and the AVR smart smoke/CO2 detector.

## Workflow

- `AGENTS.md` contains concise repository-level instructions for AI and coding agents.
- `docs/RESUME_WORKFLOW.md` contains the detailed selection, evidence-mapping, gap-question, and project-knowledge process.
- `scripts/generate_resume_artifacts.py` generates matching DOCX and PDF files from the Markdown sources.
- `.github/workflows/generate-resume-artifacts.yml` automates artifact generation after the workflow is available on the default branch.
- Targeted packages should be created against actual job listings, not speculative company names.
- Generated DOCX and PDF files must remain consistent with their Markdown sources and be visually reviewed before use.
