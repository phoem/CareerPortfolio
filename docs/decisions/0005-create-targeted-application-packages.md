# ADR 0005: Create Targeted Application Packages from Real Job Listings

## Status

Accepted

## Context

Company-specific resumes are most effective when they are built against an actual job description. Speculative company packages risk optimizing for the wrong role, level, or team.

## Decision

Create targeted application packages only when there is a concrete job listing or clearly defined role. Each package should be derived from the best-fitting canonical resume and the verified knowledge bundle.

A package may include a tailored resume, cover letter, interview notes, and generated DOCX/PDF artifacts when useful.

## Consequences

### Positive

- Improves relevance and ATS alignment.
- Avoids unnecessary speculative work.
- Preserves a clear connection between evidence and role requirements.

### Negative

- Company packages are not prebuilt before a listing exists.
- Fast-moving postings may require rapid tailoring.

## Related Decisions

- [ADR 0004: Maintain Three Canonical Generic Resumes](0004-maintain-three-canonical-generic-resumes.md)
- [ADR 0007: Use Gap Analysis Before Asking Questions](0007-use-gap-analysis-before-asking-questions.md)
