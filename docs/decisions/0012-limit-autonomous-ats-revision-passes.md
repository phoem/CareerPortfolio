# ADR 0012: Limit Autonomous ATS Revision Passes

## Status

Accepted

## Context

CareerPortfolio's ATS validation workflow may identify multiple rounds of fixable issues. Without a hard stopping rule, an automated agent could repeatedly rescore and rewrite a resume, creating churn, overfitting to the heuristic score, or an infinite revision loop.

The system must improve resumes proactively while preserving factual accuracy and requiring human review when further progress is uncertain or diminishing.

## Decision

Limit autonomous ATS-driven resume revision to a maximum of **three consecutive revision passes without human interaction**.

A revision pass consists of:

1. reviewing the current validation report;
2. making one coherent set of supported changes;
3. regenerating the Markdown-derived DOCX and PDF artifacts;
4. rerunning ATS readiness validation.

The agent must stop before three passes when any stop condition is met:

- the resume reaches the configured submission threshold;
- no material score improvement is achieved in a pass;
- remaining deductions require new user knowledge or clarification;
- further edits would risk keyword stuffing, reduced readability, unsupported claims, or factual distortion;
- the remaining gap is a genuine qualification gap rather than a presentation problem;
- the agent concludes that no responsible improvement remains.

After the third autonomous pass, the agent must stop and provide a human-review report containing:

- score history for each pass;
- changes made in each pass;
- remaining deductions and their causes;
- questions requiring user input;
- recommended next actions;
- a final recommendation: submit, revise with user input, or do not submit.

The retry counter resets after meaningful human input, including confirmation of a proposed direction, answers to gap questions, or newly documented experience.

## Consequences

### Positive

- Prevents infinite or low-value revision loops.
- Reduces overfitting to a heuristic score.
- Preserves readability and factual integrity.
- Gives the user clear control over additional iterations.
- Produces an auditable score and change history.

### Negative

- Some resumes may stop below the preferred threshold even when another pass could produce a small improvement.
- The user may need to explicitly authorize further work after the limit is reached.

## Related Decisions

- [ADR 0003: Record Knowledge Before Generating Artifacts](0003-knowledge-before-artifacts.md)
- [ADR 0006: Store Only Confirmed Knowledge](0006-store-only-confirmed-knowledge.md)
- [ADR 0007: Use Gap Analysis Before Asking Questions](0007-use-gap-analysis-before-asking-questions.md)
- [ADR 0011: Use Transparent ATS Readiness Validation](0011-use-transparent-ats-readiness-validation.md)
