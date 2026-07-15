# Architecture Decision Records

This directory records significant structural and workflow decisions for CareerPortfolio.

ADRs are immutable historical records. When a decision changes, add a new ADR that supersedes the earlier one rather than rewriting history. Minor corrections and clarifications may be made in place.

## Status values

- **Proposed** — under consideration.
- **Accepted** — approved and active.
- **Deprecated** — retained for history but no longer recommended.
- **Superseded** — replaced by a later ADR.
- **Rejected** — considered but not adopted.

## Index

| ADR | Decision | Status |
|---|---|---|
| [0001](0001-adopt-google-cloud-open-knowledge-format.md) | Adopt Google Cloud Open Knowledge Format | Accepted |
| [0002](0002-use-careerportfolio-as-the-authoritative-system.md) | Use CareerPortfolio as the authoritative professional system | Accepted |
| [0003](0003-knowledge-before-artifacts.md) | Record knowledge before generating artifacts | Accepted |
| [0004](0004-maintain-three-canonical-generic-resumes.md) | Maintain three canonical generic resumes | Accepted |
| [0005](0005-create-targeted-application-packages.md) | Create targeted application packages from real job listings | Accepted |
| [0006](0006-store-only-confirmed-knowledge.md) | Store only confirmed knowledge and preserve uncertainty | Accepted |
| [0007](0007-use-gap-analysis-before-asking-questions.md) | Use evidence-gap analysis before asking questions | Accepted |
| [0008](0008-grow-the-knowledge-base-incrementally.md) | Grow the knowledge base incrementally | Accepted |
| [0009](0009-centralize-verified-career-metrics.md) | Centralize verified career metrics | Accepted; implementation pending |
| [0010](0010-centralize-confirmed-technology-experience.md) | Centralize confirmed technology experience | Accepted; implementation pending |
| [0011](0011-use-transparent-ats-readiness-validation.md) | Use transparent ATS readiness validation | Accepted; automation pending |
| [0012](0012-limit-autonomous-ats-revision-passes.md) | Limit autonomous ATS revision passes | Accepted |
| [0013](0013-track-current-and-historical-ats-scores.md) | Track current and historical ATS scores | Accepted; automation pending |
| [0014](0014-group-process-documents-under-workflows.md) | Group process documents under `docs/workflows/` | Accepted |
| [0015](0015-organize-targeted-applications-by-company-and-posting.md) | Organize targeted applications by company and posting | Accepted |
| [0016](0016-support-selectable-resume-designs.md) | Support selectable resume designs | Accepted |
| [0017](0017-use-incremental-artifact-builds-and-scoped-validation.md) | Use incremental artifact builds and scoped validation | Accepted |

## Creating a new ADR

1. Choose the next four-digit number.
2. Use a lowercase hyphenated filename: `NNNN-short-decision-name.md`.
3. Copy the structure used by the existing records.
4. Add the ADR to this index.
5. Link related ADRs where helpful.
6. Do not renumber existing ADRs.
