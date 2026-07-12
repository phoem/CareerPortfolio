# ADR 0009: Centralize Verified Career Metrics

## Status

Accepted; implementation pending

## Context

Scale and outcome metrics appear across multiple resumes and project records. Repeating them independently risks drift, accidental precision, and contradictory values.

## Decision

Create a shared OKF metrics catalog for verified career numbers. Resume and project wording should reference the same canonical values, preserving estimates and ranges exactly.

The catalog should be implemented when the current repository foundation is stable and should include provenance, confidence, related concepts, and usage notes where helpful.

## Consequences

### Positive

- Reduces inconsistent numbers across artifacts.
- Makes estimates and exact values easier to distinguish.
- Simplifies future resume validation.

### Negative

- Introduces another shared source that must be maintained.
- Existing project concepts may still retain contextual copies of metrics.

## Related Decisions

- [ADR 0003: Knowledge Before Artifacts](0003-knowledge-before-artifacts.md)
- [ADR 0006: Store Only Confirmed Knowledge](0006-store-only-confirmed-knowledge.md)
