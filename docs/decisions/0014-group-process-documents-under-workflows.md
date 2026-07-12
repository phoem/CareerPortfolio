# ADR 0014: Group Process Documents Under docs/workflows

## Status

Accepted

## Context

CareerPortfolio documentation now includes multiple kinds of material: operating workflows, format conventions, starter instructions, roadmap items, and Architecture Decision Records. Keeping every document directly under `docs/` makes the distinction between executable processes and reference material less clear as the repository grows.

## Decision

Store repeatable process documents under `docs/workflows/`.

The initial workflow documents are:

- `docs/workflows/RESUME_WORKFLOW.md`;
- `docs/workflows/ATS_VALIDATION.md`.

Keep non-workflow reference material at the appropriate existing locations:

- `docs/OKF_PORTFOLIO.md` for OKF conventions;
- `docs/STARTER_GUIDE.md` for human onboarding;
- `docs/ROADMAP.md` for deferred ideas;
- `docs/decisions/` for ADRs.

When adding a new document, place it under `docs/workflows/` only when it defines a repeatable end-to-end or quality-gate process.

## Consequences

### Positive

- separates process documentation from conventions and reference material;
- scales cleanly as interview, LinkedIn, promotion, or other workflows are added;
- makes the starter kit easier to understand;
- provides predictable locations for agents and humans.

### Negative

- existing links and instructions must be updated when files move;
- the additional directory is unnecessary when only one workflow exists, but justified now that multiple workflows are present.

## Related Decisions

- [ADR 0002: Use CareerPortfolio as the Authoritative Professional System](0002-use-careerportfolio-as-the-authoritative-system.md)
- [ADR 0003: Record Knowledge Before Generating Artifacts](0003-knowledge-before-artifacts.md)
- [ADR 0011: Use Transparent ATS Readiness Validation](0011-use-transparent-ats-readiness-validation.md)