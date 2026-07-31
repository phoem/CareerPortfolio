# ADR 0023: Commit Every Retained ATS Validation Pass

## Status

Accepted

## Context

CareerPortfolio stores a current ATS report and an append-only score history.
Each history entry includes hashes for the source and generated artifacts.

Hashes can prove whether a later file is identical to a scored artifact, but
they cannot reconstruct content after a later revision overwrites the Markdown,
DOCX, or PDF. A local multi-pass revision loop could therefore record a useful
baseline score and then destroy the only exact copy of that baseline before the
work was committed.

Git is already the repository's versioning system and generated resume
artifacts are intentionally committed. Meaningful ATS baselines and revision
passes should use Git as the content-retention layer rather than creating a
parallel snapshot directory.

## Decision

Treat the initial ATS baseline and every meaningful retained revision pass as a
mandatory Git commit boundary.

For a local or agent-driven loop:

1. generate only the scoped Markdown-derived artifacts;
2. validate the exact rebuilt-artifact manifest;
3. update the current report, machine-readable result, and append-only history;
4. complete factual and visual review;
5. commit the source, generated artifacts, validation files, synchronized
   evidence map, and any supporting OKF changes;
6. verify the commit succeeded before beginning another pass.

The next pass must not overwrite or regenerate the same resume until the prior
pass has been committed.

Retained pass commits must not be amended, squashed, or replaced by one final
aggregate commit. Recommended commit subjects identify the application,
baseline or revision-pass number, and score.

Duplicate validations with no meaningful input or scoring-model change remain
excluded from history and do not require a new commit.

In GitHub Actions, a pass may be preserved by a short chain consisting of the
triggering source commit, the generated-artifact commit, and the validation
report commit. The next revision must not be pushed until that chain completes.

Artifact hashes remain in ATS history as integrity identifiers. Git commits are
the authoritative recovery mechanism for old source and binary artifact
versions.

## Consequences

### Positive

- Every retained score maps to recoverable Markdown, DOCX, and PDF content.
- Git can show exact source diffs between ATS passes.
- Historical binary artifacts can be checked out for visual or parser review.
- The three-pass autonomous limit becomes fully auditable.
- No duplicate snapshot-directory convention is required.

### Negative

- Multi-pass resume work creates more commits on `main`.
- Automated passes may use multiple commits to preserve one logical version.
- Agents and users must wait for the prior CI chain before pushing the next
  revision.
- Accidental history rewriting would destroy part of the audit trail and is
  therefore prohibited for retained pass commits.

## Related Decisions

- [ADR 0011: Use Transparent ATS Readiness Validation](0011-use-transparent-ats-readiness-validation.md)
- [ADR 0012: Limit Autonomous ATS Revision Passes](0012-limit-autonomous-ats-revision-passes.md)
- [ADR 0013: Track Current and Historical ATS Scores](0013-track-current-and-historical-ats-scores.md)
- [ADR 0017: Use Incremental Artifact Builds and Scoped Validation](0017-use-incremental-artifact-builds-and-scoped-validation.md)
