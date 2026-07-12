# ADR 0006: Store Only Confirmed Knowledge and Preserve Uncertainty

## Status

Accepted

## Context

Resume tailoring creates pressure to fill gaps with plausible but unverified details. That risks inaccurate claims, inconsistent metrics, and poor interview outcomes.

## Decision

Store only information confirmed by Jordan or supported by a reliable source. Do not infer technologies, features, metrics, ownership, dates, or outcomes merely because they would be typical.

Preserve estimates and ranges as estimates and ranges. Put potentially useful unknown details under `Open Questions` rather than converting them into factual prose.

## Consequences

### Positive

- Protects credibility and interview readiness.
- Makes every resume claim traceable to documented evidence.
- Reduces contradictions across artifacts.

### Negative

- Some documents may remain intentionally incomplete.
- Stronger claims may require additional questions and evidence.

## Related Decisions

- [ADR 0001: Adopt Google Cloud Open Knowledge Format](0001-adopt-google-cloud-open-knowledge-format.md)
- [ADR 0003: Knowledge Before Artifacts](0003-knowledge-before-artifacts.md)
