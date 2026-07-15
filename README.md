# CareerPortfolio

**CareerPortfolio** is the authoritative knowledge base for Jordan Newman's professional experience. It contains structured project knowledge, verified engineering accomplishments, canonical resumes, interview-preparation material, and company-specific application packages.

Resumes, cover letters, and related career artifacts are derived from the curated knowledge in this repository.

## Canonical Generic Resumes

| Document | Markdown | DOCX | PDF |
|---|---:|---:|---:|
| Senior Software Engineer | `generic/Jordan_Newman_Generic_Senior_Software_Engineer_Resume.md` | `generic/Jordan_Newman_Generic_Senior_Software_Engineer_Resume.docx` | `generic/Jordan_Newman_Generic_Senior_Software_Engineer_Resume.pdf` |
| Software Architect | `generic/Jordan_Newman_Generic_Software_Architect_Resume.md` | `generic/Jordan_Newman_Generic_Software_Architect_Resume.docx` | `generic/Jordan_Newman_Generic_Software_Architect_Resume.pdf` |
| Backend / Infrastructure | `generic/Jordan_Newman_Generic_Backend_Infrastructure_Resume.md` | `generic/Jordan_Newman_Generic_Backend_Infrastructure_Resume.docx` | `generic/Jordan_Newman_Generic_Backend_Infrastructure_Resume.pdf` |

## Targeted Application Packages

Targeted applications live under:

```text
applications/<company>/<requisition-or-role>/
```

Every posting receives a separate package with its own exact job description, resume, cover letter, ATS report and history, and optional design selection. Multiple roles at the same company never share or overwrite one `JOB_DESCRIPTION.md`.

### Netflix — JR39731 Compute Runtime

| Document | Path |
|---|---|
| Package | `applications/netflix/JR39731-compute-runtime/` |
| Resume source | `applications/netflix/JR39731-compute-runtime/Jordan_Newman_Netflix_Compute_Runtime_Resume.md` |
| Cover-letter source | `applications/netflix/JR39731-compute-runtime/Jordan_Newman_Netflix_Compute_Runtime_Cover_Letter.md` |
| Job description | `applications/netflix/JR39731-compute-runtime/JOB_DESCRIPTION.md` when restored |
| Validation | `applications/netflix/JR39731-compute-runtime/validation/` |

The employer posting associated with requisition JR39731 was verified as a Compute Runtime distributed-systems role; the package is intentionally not positioned as an Open Connect application.

### 1Password — Senior Developer, Partnerships Engineering

| Document | Path |
|---|---|
| Package | `applications/1password/7bbbdf90-partnerships-engineering/` |
| Resume source | `applications/1password/7bbbdf90-partnerships-engineering/Jordan_Newman_1Password_Partnerships_Engineering_Resume.md` |
| Job description | `applications/1password/7bbbdf90-partnerships-engineering/JOB_DESCRIPTION.md` |
| Validation | `applications/1password/7bbbdf90-partnerships-engineering/validation/` |

### Starlink — Embedded Software Engineer

| Document | Path |
|---|---|
| Package | `applications/starlink/embedded-software-engineer/` |
| ATS resume source | `applications/starlink/embedded-software-engineer/Jordan_Newman_Starlink_ATS_Resume.md` |
| Recruiter resume source | `applications/starlink/embedded-software-engineer/Jordan_Newman_Starlink_Recruiter_2Page_Resume.md` |
| Cover-letter source | `applications/starlink/embedded-software-engineer/Jordan_Newman_Starlink_Cover_Letter.md` |
| Job-source status | Exact historical posting and requisition not yet recovered |
| Validation | `applications/starlink/embedded-software-engineer/validation/` |

## Resume Designs

Reusable rendering designs live under `designs/`.

- `designs/default.json` selects the repository default.
- `applications/.../DESIGN.json` persistently selects a design for all future rebuilds of one application.
- `applications/.../DESIGN_NEXT.json` selects a design for only the next successful build and is then consumed.

See `designs/README.md` and ADR 0016.

## Career Knowledge Base

The `knowledge/` directory is the factual source of truth for project descriptions used across resumes and interview preparation.

It is maintained as a Google Cloud Open Knowledge Format (OKF) v0.1 knowledge bundle:

- concepts are Markdown files with YAML frontmatter;
- every concept includes a required `type` field;
- `knowledge/index.md` provides progressive-disclosure navigation;
- `knowledge/log.md` records meaningful knowledge updates;
- ordinary Markdown links connect related projects and systems;
- confirmed information is recorded while unknown details remain omitted or listed as open questions.

Current entries include PrimeHTTPD, the CDN platform, VirtualDir, PrimeDump, PrimeDNSTop, KeepClean, StatCache, TAFOS, and the AVR smart smoke/CO2 detector.

## Workflow and Governance

- `AGENTS.md` contains concise repository-level instructions for AI and coding agents.
- `docs/workflows/RESUME_WORKFLOW.md` contains the detailed selection, evidence-mapping, gap-question, and knowledge-capture process.
- `docs/workflows/ATS_VALIDATION.md` defines the ATS compatibility, job-alignment, revision-loop, and score-history process.
- `docs/OKF_PORTFOLIO.md` documents the repository-specific OKF conventions.
- `docs/STARTER_GUIDE.md` explains how another person can bootstrap their own CareerPortfolio.
- `docs/ROADMAP.md` records deferred enhancements and promotion criteria without prematurely adding structure.
- `docs/decisions/README.md` indexes the Architecture Decision Records that explain significant repository decisions.
- `scripts/generate_resume_artifacts.py` generates matching DOCX and PDF files for explicitly selected Markdown sources.
- `.github/workflows/generate-resume-artifacts.yml` rebuilds only sources changed on `main`; repository-wide rebuilds require an explicitly approved manual dispatch.
- `.github/workflows/validate-resumes.yml` is called with the exact build manifest and validates only resumes rebuilt by that run.
- Generated DOCX and PDF files must remain consistent with their Markdown sources and be visually reviewed before use.

## Repository

`phoem/CareerPortfolio`
