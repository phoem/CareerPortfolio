# ADR 0024: Use CI as the Single Writer for Resume-Pass Outputs

## Status

Accepted

## Context

ADR 0023 requires every retained ATS baseline and revision pass to be preserved
in Git. CareerPortfolio supports both local artifact generation and GitHub
Actions generation, but allowing both paths to write tracked DOCX, PDF, and ATS
files during the same pass creates two writers for `main`.

This race occurred after a local workflow commit was created while GitHub
Actions was still appending generated-artifact and validation commits. The
local and remote histories diverged from the same parent and required a merge.
Local Microsoft Word conversion and CI LibreOffice conversion may also produce
different binary files from identical Markdown, making concurrent artifact
ownership especially prone to conflicts.

The repository needs one predictable owner for generated outputs and a strict
serialization boundary between passes.

## Decision

Use GitHub Actions as the default and sole writer of tracked generated resume
outputs during normal ATS passes.

### Local ownership

The local user or agent:

1. starts from a clean checkout and runs `git pull --ff-only origin main`;
2. edits human-authored Markdown, evidence maps, application metadata, and
   supporting OKF knowledge;
3. commits and pushes that scoped source state;
4. makes no additional local `main` commit until the CI chain completes;
5. pulls the completed chain with `git pull --ff-only origin main`;
6. reviews the committed artifacts and validation result before starting the
   next pass.

Locally rendered artifacts may be used as temporary previews, but they are not
committed or pushed during a CI-owned pass.

### CI ownership

The generation workflow:

- checks out the exact triggering source commit;
- refuses to continue if `origin/main` has advanced;
- generates and commits only selected DOCX/PDF artifacts;
- pushes without rebasing.

The validation workflow:

- receives and checks out the exact generated-artifact commit;
- refuses to continue if `origin/main` no longer points to that commit;
- validates the exact rebuilt-artifact manifest;
- commits ATS reports, results, and histories;
- pushes without rebasing.

If `main` changes unexpectedly, CI fails safely. It does not pull, rebase, or
merge stale generated output onto newer source changes.

### Serialization

One logical pass is preserved by a linear commit chain:

```text
source/evidence commit
  -> generated-artifact commit
  -> validation-result commit
```

No next-pass or unrelated local `main` commit may be pushed until that chain
finishes. Parallel work must remain on a separate branch until CI releases
ownership of `main`.

Repository-local Git configuration should use `pull.ff=only` so an accidental
ordinary `git pull` fails instead of creating a merge commit.

## Consequences

### Positive

- Removes competing local and CI writers for generated binary artifacts.
- Produces linear, recoverable pass history.
- Prevents stale artifacts or ATS reports from being rebased onto newer source.
- Makes unexpected concurrent changes fail visibly instead of creating silent
  source/artifact mismatches.
- Preserves incremental generation and validation.

### Negative

- Each pass must wait for GitHub Actions before the next revision begins.
- Visual review occurs after pulling the CI-generated artifacts.
- CI downtime blocks normal pass completion.
- Temporary local previews cannot be treated as the committed pass artifacts.
- Parallel work requires a separate branch and delayed merge.

## Related Decisions

- [ADR 0012: Limit Autonomous ATS Revision Passes](0012-limit-autonomous-ats-revision-passes.md)
- [ADR 0017: Use Incremental Artifact Builds and Scoped Validation](0017-use-incremental-artifact-builds-and-scoped-validation.md)
- [ADR 0023: Commit Every Retained ATS Validation Pass](0023-commit-every-retained-ats-validation-pass.md)
