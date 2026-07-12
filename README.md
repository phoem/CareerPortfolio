# CareerPortfolio

**CareerPortfolio** is the authoritative knowledge base for Jordan Newman's professional experience. It contains structured project knowledge, verified engineering accomplishments, canonical resumes, interview-preparation material, and company-specific application packages.

Resumes, cover letters, and related career artifacts are derived from the curated knowledge in this repository.

## Canonical Generic Resumes

| Document | Markdown | DOCX | PDF |
|---|---:|---:|---:|
| Senior Software Engineer | `generic/Jordan_Newman_Generic_Senior_Software_Engineer_Resume.md` | `generic/Jordan_Newman_Generic_Senior_Software_Engineer_Resume.docx` | `generic/Jordan_Newman_Generic_Senior_Software_Engineer_Resume.pdf` |
| Software Architect | `generic/Jordan_Newman_Generic_Software_Architect_Resume.md` | `generic/Jordan_Newman_Generic_Software_Architect_Resume.docx` | `generic/Jordan_Newman_Generic_Software_Architect_Resume.pdf` |
| Backend / Infrastructure | `generic/Jordan_Newman_Generic_Backend_Infrastructure_Resume.md` | `generic/Jordan_Newman_Generic_Backend_Infrastructure_Resume.docx` | `generic/Jordan_Newman_Generic_Backend_Infrastructure_Resume.pdf` |

## Targeted Packages

### Netflix - Distributed Systems Engineer (L5 + L6), Compute Runtime

The employer posting associated with requisition JR39731 was verified as a Compute Runtime distributed-systems role; the package is intentionally not positioned as an Open Connect application.

| Document | Markdown | Generated DOCX | Generated PDF |
|---|---:|---:|---:|
| Resume | `netflix/Jordan_Newman_Netflix_Compute_Runtime_Resume.md` | `netflix/Jordan_Newman_Netflix_Compute_Runtime_Resume.docx` | `netflix/Jordan_Newman_Netflix_Compute_Runtime_Resume.pdf` |
| Cover Letter | `netflix/Jordan_Newman_Netflix_Compute_Runtime_Cover_Letter.md` | `netflix/Jordan_Newman_Netflix_Compute_Runtime_Cover_Letter.docx` | `netflix/Jordan_Newman_Netflix_Compute_Runtime_Cover_Letter.pdf` |

### Starlink

The existing Starlink ATS resume, recruiter resume, and cover letter remain under `starlink/`.

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
- `docs/RESUME_WORKFLOW.md` contains the detailed selection, evidence-mapping, gap-question, and knowledge-capture process.
- `docs/OKF_PORTFOLIO.md` documents the repository-specific OKF conventions.
- `docs/STARTER_GUIDE.md` explains how another person can bootstrap their own CareerPortfolio.
- `docs/ROADMAP.md` records deferred enhancements and promotion criteria without prematurely adding structure.
- `docs/decisions/README.md` indexes the Architecture Decision Records that explain significant repository decisions.
- `scripts/generate_resume_artifacts.py` generates matching DOCX and PDF files from Markdown sources.
- `.github/workflows/generate-resume-artifacts.yml` automates artifact generation after the workflow is available on the default branch.
- Targeted packages should be created against actual job listings, not speculative company names.
- Generated DOCX and PDF files must remain consistent with their Markdown sources and be visually reviewed before use.

## Repository

`phoem/CareerPortfolio`
