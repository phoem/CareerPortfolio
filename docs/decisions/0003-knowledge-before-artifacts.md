# ADR 0003: Record Knowledge Before Generating Artifacts

## Status

Accepted

## Context

Important facts can diverge when they are introduced directly into individual resumes, cover letters, or interview documents. CareerPortfolio needs one canonical location for reusable professional knowledge.

## Decision

New project facts, metrics, technologies, ownership details, and outcomes must be recorded in the OKF knowledge bundle before they are used in resumes, cover letters, interview preparation, LinkedIn content, or other generated artifacts.

The governing sequence is:

1. Confirm the information.
2. Update the relevant knowledge concept.
3. Update indexes, links, citations, and the knowledge log when appropriate.
4. Generate or revise artifacts from that knowledge.

## Consequences

### Positive

- Reduces contradictions and duplicated facts.
- Preserves information for future applications.
- Makes artifact generation more repeatable.

### Negative

- Adds a small documentation step before artifact edits.
- Urgent applications still require disciplined source updates.

## Related Decisions

- [ADR 0001: Adopt Google Cloud Open Knowledge Format](0001-adopt-google-cloud-open-knowledge-format.md)
- [ADR 0006: Store Only Confirmed Knowledge](0006-store-only-confirmed-knowledge.md)
