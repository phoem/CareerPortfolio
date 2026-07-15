# ADR 0017: Use Incremental Artifact Builds and Scoped Validation

## Status

Accepted

## Context

Artifact generation previously rediscovered and regenerated every resume and cover letter whenever any eligible source changed. The independent validation workflow then rescored every resume. This caused unnecessary binary changes, validation-history noise, longer workflow runs, and avoidable concurrent writes to `main`.

Shared generator or design changes can affect many artifacts, but rebuilding the entire repository is a consequential operation that should remain under explicit human control.

## Decision

Automatic workflow runs rebuild only artifact sources directly affected by a triggering change.

The generator emits a machine-readable manifest listing the exact Markdown sources, DOCX files, and PDF files rebuilt. ATS validation is invoked from that build and validates only resume entries in the manifest. It does not independently rediscover or rescore every resume.

A repository-wide rebuild is available only through manual workflow dispatch with the `full_rebuild` input explicitly enabled. Changes to shared generator or design infrastructure produce a full-rebuild recommendation but do not authorize or trigger one. Jordan decides whether the full rebuild occurs.

## Consequences

### Positive

- reduces workflow time and unnecessary binary churn;
- keeps ATS history focused on materially rebuilt resumes;
- couples validation to the exact artifacts it assesses;
- prevents infrastructure changes from silently rewriting every deliverable;
- preserves explicit human approval for full rebuilds.

### Negative

- shared infrastructure changes may leave existing artifacts on the prior renderer or design until a full rebuild is approved;
- workflow selection logic and the rebuilt-artifact manifest require maintenance;
- reviewers must pay attention to full-rebuild recommendations in workflow summaries.

## Related Decisions

- [ADR 0011: Use Transparent ATS Readiness Validation](0011-use-transparent-ats-readiness-validation.md)
- [ADR 0013: Track Current and Historical ATS Scores](0013-track-current-and-historical-ats-scores.md)
- [ADR 0016: Support Selectable Resume Designs](0016-support-selectable-resume-designs.md)
