# AGENTS.md

## Purpose

This repository is a living professional-knowledge, resume, and application-material system for Jordan Newman.

Agents working in this repository must preserve factual accuracy, avoid inventing experience, and tailor each resume to the target role using only documented information or facts confirmed directly by Jordan.

## Source-of-Truth Hierarchy

1. `knowledge/` is the authoritative professional-knowledge source and MUST be maintained as an Open Knowledge Format (OKF) v0.1 knowledge bundle.
2. `generic/` contains the three canonical reusable resumes:
   - Senior Software Engineer
   - Software Architect
   - Backend / Infrastructure Engineer
3. `applications/<company>/<posting>/` contains one isolated package per real job posting.
4. `designs/` contains reusable rendering designs and the repository default.
5. `docs/workflows/RESUME_WORKFLOW.md` defines the detailed operating process.
6. `docs/workflows/ATS_VALIDATION.md` defines the ATS validation and revision-loop process.
7. `docs/workflows/LINKEDIN_PROFILE_WORKFLOW.md` defines the manual LinkedIn review, approval, publishing, and verification process.
8. `docs/OKF_PORTFOLIO.md` defines the repository-specific OKF conventions.
9. `docs/decisions/` contains Architecture Decision Records for significant repository decisions.
10. `docs/ROADMAP.md` stores deferred ideas and future enhancements that are not yet justified for implementation.

## Required Behavior

- Read the exact job description before selecting a resume base.
- Create a separate application directory for every posting, even when another application exists for the same company.
- Never overwrite or combine one posting's `JOB_DESCRIPTION.md`, resume, validation score, or history with another posting.
- Compare the role requirements against all three generic resumes.
- Select the closest base resume rather than blindly reusing the most recent one.
- Traverse `knowledge/index.md` and review relevant OKF concepts before drafting claims or bullets.
- Never invent technologies, metrics, responsibilities, dates, outcomes, or project features.
- When a role needs evidence that is not documented, ask Jordan whether he has worked on a project involving the missing capability.
- If Jordan confirms relevant experience, gather only the details needed to document it accurately, update the appropriate OKF concept first, then use it in a resume.
- Leave unknown fields out rather than filling them with assumptions.
- Prefer concrete scale, architecture, implementation details, and measured outcomes when documented.
- Tailor technical depth to the audience: recruiter, ATS, hiring manager, systems engineer, or architect.
- Keep the three generic resumes broadly reusable while selectively improving each with the strongest relevant project descriptions.
- Keep targeted resumes tightly aligned to their own posting.
- Record significant structural or workflow decisions as ADRs under `docs/decisions/`.
- Put useful but premature ideas in `docs/ROADMAP.md` instead of creating speculative structure.

## Application Packages

- Use `applications/<company>/<requisition-or-role>/`.
- Include `APPLICATION.json` with company, role, requisition, job-description filename, and artifact sources.
- Store the exact posting as `JOB_DESCRIPTION.md` in that application directory.
- Store ATS reports and history under that application's `validation/` directory.
- Future interview material should remain associated with the relevant application package or link back to it unambiguously.

## Design Selection

- `designs/default.json` selects the repository default design.
- `DESIGN.json` in an application directory is persistent for all future builds of that application.
- `DESIGN_NEXT.json` is a one-build override, takes precedence, and is removed after successful generation.
- Unknown design names are errors; do not silently substitute another design.
- Designs control presentation only and must never change or invent factual resume content.

## OKF Knowledge Capture

The `knowledge/` directory targets Google Cloud's Open Knowledge Format v0.1.

- Every non-reserved Markdown concept file MUST begin with parseable YAML frontmatter.
- Every concept frontmatter block MUST contain a non-empty `type` field.
- Use `title`, `description`, `tags`, `timestamp`, and `resource` when known and useful.
- Producer-defined metadata such as `status`, `owner`, `evidence_status`, and `deployment` MAY be added.
- `index.md` and `log.md` are reserved OKF filenames and must follow OKF conventions.
- Use normal Markdown links to connect related concepts.
- Use a `# Citations` section when claims rely on external sources.
- Preserve unknown frontmatter fields when editing.
- Do not create separate `project.okf.yaml` files; OKF knowledge lives in Markdown concept documents with YAML frontmatter.

When Jordan provides new information:

1. Update the corresponding OKF concept under `knowledge/`.
2. Record factual implementation details, scale, technologies, outcomes, ownership, and operational context.
3. Preserve uncertainty explicitly where appropriate.
4. Add or update cross-links to related concepts.
5. Add resume-ready variants only when supported by documented facts.
6. Update the nearest `index.md` when a new concept is added.
7. Add a dated entry to `knowledge/log.md` for meaningful knowledge changes.
8. Grow documentation incrementally; do not require every concept to have every possible section.

## Resume Generation

- Markdown is the editable source format.
- DOCX and PDF are generated deliverables and must remain consistent with the Markdown source.
- Automatic builds MUST rebuild only resume or cover-letter sources affected by the triggering change.
- ATS validation MUST consume the exact rebuilt-artifact manifest and validate only resumes rebuilt in that run.
- A repository-wide rebuild is manual-only and requires Jordan's explicit approval through the workflow's `full_rebuild` input.
- Changes to shared generator or design infrastructure may justify recommending a full rebuild, but agents and workflows MUST NOT perform one without Jordan's approval.
- Preserve ATS-safe structure in ATS variants.
- Avoid dense keyword stuffing or unsupported claims.
- Use role-specific wording while keeping the underlying facts consistent across variants.
- Important facts must not exist only inside a resume; add them to the OKF knowledge bundle first.
- Run `docs/workflows/ATS_VALIDATION.md` before submitting targeted application materials.

## Repository Changes

- The canonical repository is `phoem/CareerPortfolio`.
- Commit directly to `main` by default unless Jordan explicitly requests a branch or pull request.
- Use clear commit messages that describe the resume, knowledge, workflow, ADR, roadmap, design, or application change.
- Do not reorganize or rename existing files without a concrete benefit and corresponding README, index, and ADR updates when appropriate.

## LinkedIn Profile Changes

- Run the LinkedIn workflow only when Jordan explicitly requests it.
- Keep the review phase read-only and present exact, evidence-supported replacement text before editing.
- Require explicit field-level approval before making any externally visible change.
- Publish only the approved wording and verify every saved field afterward.
- Never store LinkedIn credentials, cookies, session tokens, or recovery information.
- Never modify unrelated account, privacy, job-search, messaging, connection, endorsement, recommendation, or posting settings.
- Stop for renewed approval if the current profile or proposed wording materially changes after the approval gate.
