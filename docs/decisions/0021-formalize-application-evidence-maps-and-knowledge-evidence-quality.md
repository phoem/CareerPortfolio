---
type: decision
status: accepted
decision_number: 21
tags:
  - evidence
  - knowledge
  - resume-tailoring
  - workflow
---

# ADR 0021: Formalize Application Evidence Maps and Knowledge Evidence Quality

## Status

Accepted

## Context

CareerPortfolio already requires agents to map job requirements to documented professional evidence before tailoring a resume. The workflow also requires confirmed facts, preservation of uncertainty, and targeted gap questions. As application work expands, these practices need durable artifacts and clearer evidence classifications so that mappings can be reviewed, reused during ATS validation, and updated without blurring exact values, estimates, external support, or unresolved questions.

## Decision

For every targeted application, create and maintain an `EVIDENCE_MAP.md` file in the application package. It must classify each meaningful job requirement as required, preferred, or contextual and map it to resume evidence, supporting OKF concepts, documented metrics or scope, evidence strength, and any gap or follow-up action.

Knowledge concepts may explicitly classify supporting facts as exact, estimated, externally supported, or qualitative. Resume-safe wording may be recorded when it is a faithful presentation of those facts. Unresolved details that could strengthen future applications should be retained under an `Open Questions` section in the nearest relevant OKF concept rather than in a separate speculative database.

The evidence map is an intermediate tailoring artifact and a validation input. It does not replace `JOB_DESCRIPTION.md`, the OKF knowledge bundle, or the ATS report.

## Consequences

Positive:

- Makes requirement coverage and genuine gaps visible before drafting.
- Provides a reusable bridge between the job posting, OKF concepts, resume wording, and ATS validation.
- Reduces accidental conversion of estimates into exact claims.
- Preserves useful unanswered questions without blocking incremental documentation.
- Improves reviewability for recruiters, hiring managers, and technical reviewers.

Trade-offs:

- Adds one maintained Markdown artifact to every targeted application package.
- Evidence maps can become stale when the posting, knowledge, or resume changes and therefore must be reviewed during tailoring and validation.
- Evidence classifications improve discipline but do not replace human judgment about truthfulness or relevance.

## Related

- [ADR 0003: Knowledge before artifacts](0003-knowledge-before-artifacts.md)
- [ADR 0006: Store only confirmed knowledge](0006-store-only-confirmed-knowledge.md)
- [ADR 0007: Use gap analysis before asking questions](0007-use-gap-analysis-before-asking-questions.md)
- [ADR 0011: Use transparent ATS readiness validation](0011-use-transparent-ats-readiness-validation.md)
- [Resume Tailoring and Knowledge Workflow](../workflows/RESUME_WORKFLOW.md)
- [OKF Knowledge Conventions](../OKF_PORTFOLIO.md)
