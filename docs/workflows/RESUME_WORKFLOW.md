# Resume Tailoring and Knowledge Workflow

## Goals

This repository should make future resume tailoring faster, more accurate, and less repetitive by separating reusable professional knowledge from the resumes that consume it.

## Canonical Resume Set

The repository maintains three generic resumes:

1. **Senior Software Engineer** — broad software, backend, systems, security, and infrastructure roles.
2. **Software Architect** — architecture, principal-level ownership, technical leadership, platform design, and cross-team standards.
3. **Backend / Infrastructure Engineer** — backend systems, distributed infrastructure, networking, reliability, performance, CDN, and systems software.

All three should improve over time, but each should emphasize the same facts differently according to its target audience.

## Job-Tailoring Workflow

1. Read and summarize the job posting.
2. Identify required and preferred capabilities.
3. Compare those requirements against the three generic resumes.
4. Select the best base resume.
5. Traverse `knowledge/index.md` and search the OKF knowledge bundle for concepts that demonstrate the requested capabilities.
6. Create or update `EVIDENCE_MAP.md` in the application package. For every meaningful requirement, record:
   - classification as required, preferred, or contextual;
   - matching experience and intended resume evidence;
   - supporting project, role, and OKF concept;
   - documented metric, scope, or qualitative outcome;
   - evidence strength as direct, adjacent, or missing;
   - any wording, gap question, or follow-up action needed.
7. Review the evidence map for genuine gaps and stale mappings before drafting.
8. For each meaningful gap, ask Jordan whether he has worked on a project involving that capability.
9. When Jordan provides relevant experience, update the knowledge bundle before relying on it in the resume.
10. Add cross-links, citations, metadata, evidence classifications, open questions, and a log entry when the new knowledge warrants them.
11. Tailor the summary, skills order, selected highlights, project descriptions, and work-history bullets using `docs/STYLE_GUIDE.md`. Prefer the Google XYZ formula—outcome (X), verified measure or scope (Y), and method (Z)—when the documented facts support it; use an outcome-first alternative when they do not.
12. Keep `EVIDENCE_MAP.md` synchronized with the selected wording and final evidence used in the resume.
13. Produce Markdown and rebuild only the corresponding DOCX and PDF deliverables.
14. Pass the exact rebuilt-artifact manifest, job description, evidence map, and relevant OKF concepts to the ATS readiness and final-artifact validation process in `docs/workflows/ATS_VALIDATION.md`.
15. Commit the initial retained ATS baseline, including its exact source, rebuilt artifacts, validation files, evidence map, and supporting knowledge changes, before starting any revision pass.
16. Resolve critical failures and repeat validation until the application is at least Strong or Jordan explicitly approves submission with known limitations. Commit every meaningful retained revision pass before another pass changes the same resume.
17. Update the repository README and company package index when adding a new application package.

## Application Evidence Map

Every targeted application package must contain `EVIDENCE_MAP.md`. It is a reviewable bridge between the exact posting, the OKF knowledge bundle, the targeted resume, and ATS validation.

Recommended columns:

| Requirement | Class | Resume evidence | Supporting OKF concept | Metric or scope | Strength | Gap or action |
|---|---|---|---|---|---|---|

Rules:

- Use the exact posting as the source for requirement wording and classification.
- Link to the nearest supporting OKF concept rather than copying an undocumented claim into the map.
- Mark evidence `direct`, `adjacent`, or `missing` and explain borderline cases.
- Preserve estimates and ranges exactly as classified in the knowledge concept.
- Do not convert adjacent experience into a direct technology claim.
- Update the map whenever the job description, relevant knowledge, or resume wording changes materially.
- Treat a stale or materially inconsistent map as a validation issue.
- The evidence map is not a substitute for the exact `JOB_DESCRIPTION.md` or the final ATS report.

## Question Strategy

Questions should be targeted and useful. Do not ask Jordan to restate facts already documented.

Ask when:

- a required capability has no documented evidence;
- a project appears relevant but its implementation, scale, ownership, or outcome is unclear;
- a metric would materially strengthen a claim;
- wording could imply something broader than the known facts;
- the role values a technology or domain that may exist in Jordan's background but is not yet documented.

A useful gap question follows this pattern:

> Have you worked on any project involving `<missing capability>`? If so, what did you build, what part did you personally own, what technologies did you use, and was it deployed or measured in production?

Ask fewer questions when the existing knowledge base already supplies sufficient evidence.

## OKF Knowledge Base

The `knowledge/` directory is an Open Knowledge Format (OKF) v0.1 knowledge bundle based on the Google Cloud specification.

OKF uses a directory tree of Markdown files with YAML frontmatter. It does **not** use `project.okf.yaml` files.

### Bundle rules

- Each concept is a UTF-8 Markdown file.
- Every non-reserved concept file must begin with YAML frontmatter.
- `type` is required and must be non-empty.
- Recommended metadata includes `title`, `description`, `resource`, `tags`, and `timestamp`.
- Repository-specific extensions may include `status`, `owner`, `evidence_status`, `deployment`, and other useful fields.
- `index.md` is reserved for progressive-disclosure navigation.
- `log.md` is reserved for chronological knowledge updates.
- Concepts should use ordinary Markdown links to related concepts.
- External evidence should be listed under `Citations` when applicable.
- Unknown metadata and body fields must be preserved during round-trip edits.

See `docs/OKF_PORTFOLIO.md` for the local conventions used in this repository.

### Recommended body sections

Use only sections supported by known facts:

- Summary
- Problem solved
- Personal ownership
- Architecture
- Implementation details
- Technologies and platform APIs
- Production deployment and scale
- Performance and reliability
- Security or operational impact
- Relationship to other systems
- Evidence
- Resume-ready descriptions
- Interview discussion points
- Open Questions
- Citations

Not every concept needs every section immediately.

## Knowledge-Capture Workflow

When new professional information is learned:

1. Locate the existing concept through `knowledge/index.md` or create a new concept.
2. Confirm what Jordan personally designed, implemented, operated, or led.
3. Record only confirmed facts.
4. Distinguish exact values, estimates, ranges, externally supported facts, and qualitative outcomes.
5. Add or update YAML frontmatter.
6. Add links to related OKF concepts.
7. Add external citations where claims rely on published material.
8. Put unresolved but potentially valuable details under `Open Questions` rather than guessing.
9. Add resume-safe wording only when it faithfully preserves the evidence classification and personal ownership.
10. Update `knowledge/index.md` when a concept is added or materially renamed.
11. Record meaningful changes in `knowledge/log.md`.
12. Only then use the information in generic or targeted resumes.

## Resume Description Variants

Knowledge concepts may hold multiple factual wording variants:

- one-line ATS version;
- recruiter-friendly version;
- technically detailed systems version;
- architect/leadership version;
- company-specific version when justified.

These are alternate presentations of the same documented facts, not separate claims.

## ATS Readiness and Final Quality Gate

Every finished targeted resume should be validated against both the job description and the generated artifacts.

- Treat the result as a transparent heuristic readiness score, not a prediction of a specific employer's ATS ranking.
- Inspect extracted text and reading order from the actual DOCX and PDF.
- Score parseability, completeness, required evidence, preferred evidence, keyword quality, and human positioning separately.
- Use the current `EVIDENCE_MAP.md` as the starting requirement-to-evidence matrix and verify it against the resume and OKF concepts.
- Report critical failures and prioritized recommendations.
- Never improve a score by inventing experience or inserting unsupported keywords.
- Mark a resume Not Ready when the artifacts fail to parse, the wrong role is targeted, unsupported claims appear, or the generated files disagree materially with the Markdown source.

See `docs/workflows/ATS_VALIDATION.md` and ADR 0011 for the full model.

## Accuracy Rules

- Never infer that a feature existed solely because it would be typical for that system.
- Never convert estimates into exact values.
- Preserve ranges such as `3,000-4,000 servers` when that is the known estimate.
- Distinguish personal implementation from team or company ownership.
- Avoid claiming benchmark leadership unless a reproducible or contemporaneous basis is documented.
- Prefer precise APIs and mechanisms when known, such as `kqueue`, `sendfile()`, `SF_NODISKIO`, `TCP_NOPUSH`, `TCP_NODELAY`, `O_NONBLOCK`, and `accept_filter_http`.
- Important professional knowledge must not live only in a resume.

## Decisions and Deferred Ideas

- Significant structural and workflow decisions must be recorded as Architecture Decision Records under `docs/decisions/`.
- Use the next sequential four-digit ADR number and update `docs/decisions/README.md`.
- Do not rewrite accepted ADR history when a decision changes; add a new ADR that supersedes the old one.
- Useful ideas that do not yet justify implementation belong in `docs/ROADMAP.md`.
- Promote roadmap items into implementation only when they solve a demonstrated need or Jordan explicitly prioritizes them.

## Maintenance

When new facts are learned:

1. Update the OKF knowledge base.
2. Determine whether one or more generic resumes should be improved.
3. Update only the generic versions for which the information strengthens the intended positioning.
4. Regenerate only the matching DOCX and PDF files whose sources changed.
5. Run ATS readiness and final-artifact validation only for resumes included in that rebuild.
6. Record the knowledge change in `knowledge/log.md` when meaningful.
7. Record significant repository decisions in an ADR.
8. Commit the complete retained baseline or revision-pass state with a message that identifies the resume, pass, and score before beginning another pass.

## Incremental Builds and Full Rebuilds

Normal pushes rebuild only artifact sources directly affected by the change. A changed resume or cover-letter Markdown source rebuilds itself; an application manifest or application-specific design selection rebuilds the artifact sources in that application package.

Changes to shared generator code or shared designs do not automatically rebuild the repository. The workflow reports that a full rebuild may be warranted, and the agent should explain the impact and recommend one when appropriate. A full rebuild remains Jordan's decision and may run only through an explicit manual workflow dispatch with `full_rebuild` enabled.

The generator emits a manifest containing the exact sources, DOCX files, and PDF files rebuilt. Validation must use that manifest rather than rediscovering every resume in the repository.
