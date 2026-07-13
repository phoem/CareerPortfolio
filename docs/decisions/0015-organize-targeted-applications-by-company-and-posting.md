# ADR 0015: Organize Targeted Applications by Company and Posting

## Status

Accepted

## Context

A company may have multiple open roles, requisitions, resume variants, job descriptions, validation histories, and interview materials. A single root-level company directory and one `JOB_DESCRIPTION.md` cannot represent multiple applications without overwriting or mixing evidence.

## Decision

Store targeted application packages under:

```text
applications/<company>/<posting-slug>/
```

The posting slug should use the requisition identifier when available, followed by a concise role slug, for example:

```text
applications/netflix/JR39731-compute-runtime/
```

Each posting directory owns its own:

- `APPLICATION.json` manifest;
- exact `JOB_DESCRIPTION.md`;
- resume and cover-letter sources and generated artifacts;
- ATS validation report and history;
- optional application-specific design selection;
- future interview materials related to that posting.

A new posting for the same company creates a sibling directory. It never overwrites or appends to another posting's job-description file.

## Consequences

### Positive

- preserves every job description independently;
- prevents resumes and validation scores from being compared with the wrong posting;
- supports multiple simultaneous applications to one company;
- gives future interview materials an unambiguous application context;
- keeps company names out of the repository root.

### Negative

- paths are longer;
- legacy root-level company directories require migration;
- scripts and workflows must discover application manifests recursively.

## Related Decisions

- [ADR 0005: Create Targeted Application Packages](0005-create-targeted-application-packages.md)
- [ADR 0011: Use Transparent ATS Readiness Validation](0011-use-transparent-ats-readiness-validation.md)
- [ADR 0013: Track Current and Historical ATS Scores](0013-track-current-and-historical-ats-scores.md)
