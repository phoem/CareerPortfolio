# ADR 0013: Track Current and Historical ATS Scores

## Status

Accepted

## Context

ATS validation produces useful category scores and recommendations, but a single current score does not show whether a resume is improving, regressing, or being overfit through repeated edits.

Generic resumes and targeted resumes also serve different purposes. A generic resume has no single job description against which to measure job alignment, while a targeted resume does.

## Decision

Track both the **current ATS validation result** and a compact **validation history** for each resume, with different score types for generic and targeted resumes.

### Generic resumes

Generic resumes track a **baseline ATS compatibility score** covering:

- artifact parseability and reading order;
- required-information completeness;
- conventional section structure;
- Markdown, DOCX, and PDF consistency;
- general language quality and readability.

Generic resumes do not receive a job-specific alignment score unless evaluated against a specific posting.

### Targeted resumes

Targeted resumes track the full **job-specific readiness score**, including:

- artifact parseability and structure;
- required-information completeness;
- required job-requirement evidence;
- preferred job-requirement evidence;
- language and keyword quality;
- human readability and positioning.

### Current result

Each resume keeps one current summary containing:

- validation date;
- validator or tool version;
- overall score;
- category scores;
- disposition;
- job identifier or job-description hash for targeted resumes;
- artifact hashes or source commit when practical;
- link to the full validation report.

### History

Keep an append-only compact history for meaningful validation runs. Each entry records:

- timestamp;
- source commit or artifact version;
- job identifier for targeted resumes;
- overall score;
- category scores;
- disposition;
- revision-pass number;
- brief summary of changes since the prior run.

Do not store every experimental or duplicate run. Record the initial baseline, each autonomous revision pass, any run after meaningful human input, and the final pre-submission result.

### Suggested paths

Targeted resume:

```text
applications/<company>/<role>/validation/
    ATS_REPORT.md
    ATS_HISTORY.md
```

Existing company-specific directories may use the same `validation/` subdirectory until the broader `applications/` layout is adopted.

Generic resume:

```text
generic/validation/
    <resume-name>-ATS_REPORT.md
    <resume-name>-ATS_HISTORY.md
```

A future machine-readable summary may be added if automation requires it, but Markdown remains the reviewable source until then.

## Consequences

### Positive

- Shows whether revisions materially improve a resume.
- Makes the three-pass retry limit auditable.
- Helps detect regressions after later edits.
- Separates general ATS compatibility from role-specific alignment.
- Preserves a useful pre-submission record.

### Negative

- Adds maintenance and generated-report files.
- Scores can become stale when the job description, source resume, or scoring model changes.
- Historical scores from different validator versions may not be directly comparable.

## Guardrails

- A score is valid only for the recorded resume version, artifact set, job description, and validator version.
- Changing the scoring model must be recorded and clearly marked in later history entries.
- Do not compare a generic baseline score directly with a targeted job-specific score.
- Do not optimize for score at the expense of accuracy or readability.

## Related Decisions

- [ADR 0011: Use Transparent ATS Readiness Validation](0011-use-transparent-ats-readiness-validation.md)
- [ADR 0012: Limit Autonomous ATS Revision Passes](0012-limit-autonomous-ats-revision-passes.md)
