# Resume Tailoring and Knowledge Workflow

## Goals

This repository should make future resume tailoring faster, more accurate, and less repetitive by separating reusable project knowledge from the resumes that consume it.

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
5. Traverse `portfolio/index.md` and search the OKF project bundle for concepts that demonstrate the requested capabilities.
6. Build a factual evidence map:
   - requirement
   - matching experience
   - supporting project or role
   - documented metric or outcome
   - supporting OKF concept
7. Identify gaps.
8. For each meaningful gap, ask Jordan whether he has worked on a project involving that capability.
9. When Jordan provides relevant experience, update the project portfolio before relying on it in the resume.
10. Add cross-links, citations, metadata, and a log entry when the new knowledge warrants them.
11. Tailor the summary, skills order, selected highlights, project descriptions, and work-history bullets.
12. Produce Markdown, DOCX, and PDF deliverables as required.
13. Update the repository README and company package index when adding a new application package.

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

Ask fewer questions when the existing portfolio already supplies sufficient evidence.

## OKF Project Portfolio

The `portfolio/` directory is an Open Knowledge Format (OKF) v0.1 knowledge bundle based on the Google Cloud specification.

OKF uses a directory tree of Markdown files with YAML frontmatter. It does **not** use `project.okf.yaml` files.

### Bundle rules

- Each project concept is a UTF-8 Markdown file.
- Every non-reserved concept file must begin with YAML frontmatter.
- `type` is required and must be non-empty.
- Recommended metadata includes `title`, `description`, `resource`, `tags`, and `timestamp`.
- Repository-specific extensions may include `status`, `owner`, `evidence_status`, `deployment`, and other useful fields.
- `index.md` is reserved for progressive-disclosure navigation.
- `log.md` is reserved for chronological knowledge updates.
- Concepts should use ordinary Markdown links to related concepts.
- External evidence should be listed under `# Citations` when applicable.
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
- Resume-ready descriptions
- Interview discussion points
- Open questions for future documentation
- Citations

Not every project needs every section immediately.

## Knowledge-Capture Workflow

When new project information is learned:

1. Locate the existing concept through `portfolio/index.md` or create a new project concept.
2. Confirm what Jordan personally designed, implemented, operated, or led.
3. Record only confirmed facts.
4. Distinguish exact values, estimates, ranges, and qualitative outcomes.
5. Add or update YAML frontmatter.
6. Add links to related OKF concepts.
7. Add external citations where claims rely on published material.
8. Put unresolved but potentially valuable details under `Open Questions` rather than guessing.
9. Update `portfolio/index.md` when a concept is added or materially renamed.
10. Record meaningful changes in `portfolio/log.md`.
11. Only then use the information in generic or targeted resumes.

## Resume Description Variants

Project concepts may hold multiple factual wording variants:

- one-line ATS version;
- recruiter-friendly version;
- technically detailed systems version;
- architect/leadership version;
- company-specific version when justified.

These are alternate presentations of the same documented facts, not separate claims.

## Accuracy Rules

- Never infer that a feature existed solely because it would be typical for that system.
- Never convert estimates into exact values.
- Preserve ranges such as `3,000-4,000 servers` when that is the known estimate.
- Distinguish personal implementation from team or company ownership.
- Avoid claiming benchmark leadership unless a reproducible or contemporaneous basis is documented.
- Prefer precise APIs and mechanisms when known, such as `kqueue`, `sendfile()`, `SF_NODISKIO`, `TCP_NOPUSH`, `TCP_NODELAY`, `O_NONBLOCK`, and `accept_filter_http`.
- Important project knowledge must not live only in a resume.

## Maintenance

When new facts are learned:

1. Update the OKF project portfolio.
2. Determine whether one or more generic resumes should be improved.
3. Update only the generic versions for which the information strengthens the intended positioning.
4. Regenerate matching DOCX and PDF files.
5. Record the knowledge change in `portfolio/log.md` when meaningful.
6. Commit with a clear message.
