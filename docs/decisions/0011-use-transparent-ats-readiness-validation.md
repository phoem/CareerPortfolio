# ADR 0011: Use Transparent ATS Readiness Validation

## Status

Accepted; automation pending

## Context

CareerPortfolio needs a repeatable way to decide whether a finished resume is ready to submit. Commercial resume scanners often present a single opaque "ATS score," but applicant-tracking systems vary by employer, vendor, configuration, and recruiter workflow. A universal score would imply certainty the system cannot provide.

The validation process must also protect the existing accuracy rules. It must never improve a score by inventing experience, adding unsupported keywords, or overstating evidence.

## Decision

CareerPortfolio will use a transparent heuristic **ATS readiness validation** process rather than claim to reproduce or predict a specific employer's ATS ranking.

The process will evaluate:

- generated DOCX and PDF parseability;
- document structure and required information;
- mapping of required and preferred job capabilities to verified evidence;
- natural, accurate keyword use;
- human readability and role-specific positioning;
- consistency among Markdown, DOCX, and PDF artifacts.

The report will provide category scores, supporting findings, critical failures, prioritized recommendations, and an overall readiness score. A numeric score alone is never sufficient.

Automated checks may be added in `scripts/validate_resume.py`, but human or agent judgment remains required for truthfulness, relevance, evidence strength, and narrative quality.

## Consequences

### Positive

- creates a repeatable final quality gate before submission;
- exposes why a resume scored well or poorly;
- separates parsing compatibility from job alignment;
- catches generated-artifact failures that source-only review misses;
- supports iterative improvement without unsupported keyword stuffing;
- can eventually run locally or in GitHub Actions.

### Negative

- the score cannot guarantee an interview or replicate an employer's private system;
- requirement extraction and evidence strength still require judgment;
- PDF and DOCX parsing add implementation dependencies;
- scoring weights may need refinement as the workflow is used.

## Related Documentation

- [ATS Validation Workflow](../workflows/ATS_VALIDATION.md)
- [Resume Tailoring and Knowledge Workflow](../workflows/RESUME_WORKFLOW.md)
- [ADR 0003: Knowledge Before Artifacts](0003-knowledge-before-artifacts.md)
- [ADR 0006: Store Only Confirmed Knowledge](0006-store-only-confirmed-knowledge.md)
- [ADR 0007: Use Gap Analysis Before Asking Questions](0007-use-gap-analysis-before-asking-questions.md)