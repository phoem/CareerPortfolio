# Application Status Workflow

## Purpose

Application status is distinct from resume-preparation status. A package can be submission ready without proof that an application was submitted. This workflow records only confirmed application lifecycle facts and preserves uncertainty explicitly.

## Source of truth

Each application package contains an authoritative `APPLICATION_STATUS.json` beside `APPLICATION.json`:

```json
{
  "schema_version": 1,
  "status": "not_applied"
}
```

`applications/STATUS.json` is a generated portfolio-wide index. Never edit the master index directly. Refresh it after changing a package status:

```text
python scripts/update_application_status.py
```

Validate all package records and confirm that the master index is current:

```text
python scripts/update_application_status.py --check
```

## Status values

- `unknown` — the historical application state has not been confirmed. Existing packages use this during migration unless reliable evidence establishes another state.
- `not_applied` — the application is known not to have been submitted. New packages start here unless they represent an already-submitted application.
- `applied` — submission is confirmed, with no later confirmed stage.
- `interviewing` — at least one interview or active interview-stage step is confirmed.
- `offer_received` — an offer is confirmed and no final outcome has been recorded.
- `closed` — the application process has ended. Record an `outcome` when known.

Allowed `outcome` values are:

- `not_selected`
- `withdrawn`
- `offer_declined`
- `accepted`

An outcome is valid only with `status: closed`.

## Evidence and uncertainty rules

- Never infer submission from a completed resume, cover letter, ATS score, application package, or `Submission ready` preparation state.
- Never change `unknown` to `not_applied` without confirmation.
- Use `not_applied` by default only for newly created packages whose submission is being tracked from creation.
- Record a known lifecycle event date as `history.occurred_at`. Omit it when unknown rather than estimating it.
- A direct statement from Jordan is sufficient confirmation. Preserve the confirmation in `history.source`.
- `recorded_at` is when the fact was entered into CareerPortfolio; it is not an inferred submission, interview, offer, or outcome date.
- `occurred_at`, when present, is the confirmed date or datetime when the lifecycle event actually happened.
- Keep preparation status in package documentation or the application queue; do not put it in `APPLICATION_STATUS.json`.

## History

Use `history` when a confirmed transition should be retained:

```json
{
  "schema_version": 1,
  "status": "closed",
  "outcome": "not_selected",
  "history": [
    {
      "status": "applied",
      "recorded_at": "2026-08-11",
      "source": "Portfolio owner",
      "note": "Application date is not documented."
    },
    {
      "status": "closed",
      "outcome": "not_selected",
      "recorded_at": "2026-08-11",
      "source": "Portfolio owner",
      "note": "Outcome date is not documented."
    }
  ]
}
```

The top-level `status` and optional `outcome` must match the final history event.

## New application packages

1. Create `APPLICATION.json` and capture the exact posting.
2. Create `APPLICATION_STATUS.json` with `schema_version: 1` and `status: not_applied`, unless the package is being created for a previously submitted application whose state is confirmed.
3. Complete the tailoring and validation workflow independently of application status.
4. Refresh `applications/STATUS.json`.
5. Run the status checker before committing.

Status-only changes do not rebuild resumes or cover letters.
