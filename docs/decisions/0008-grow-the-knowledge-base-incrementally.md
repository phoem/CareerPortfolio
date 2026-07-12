# ADR 0008: Grow the Knowledge Base Incrementally

## Status

Accepted

## Context

Documenting every possible project detail in advance would create unnecessary work and encourage speculative structure. CareerPortfolio should become more complete as real applications and interviews reveal useful gaps.

## Decision

Grow the OKF knowledge bundle incrementally. Record confirmed information currently known, leave unknown details out or list them as open questions, and expand concepts when a real job, interview, or artifact requires deeper evidence.

Do not require every concept to contain every possible section. Do not create future directories or workflows until they solve a demonstrated need; record deferred ideas in `docs/ROADMAP.md`.

## Consequences

### Positive

- Keeps the repository useful and manageable.
- Prioritizes knowledge with immediate career value.
- Avoids overengineering and invented completeness.

### Negative

- Some concepts remain partial for extended periods.
- New applications may expose gaps that require additional discussion.

## Related Decisions

- [ADR 0006: Store Only Confirmed Knowledge](0006-store-only-confirmed-knowledge.md)
- [ADR 0007: Use Gap Analysis Before Asking Questions](0007-use-gap-analysis-before-asking-questions.md)
