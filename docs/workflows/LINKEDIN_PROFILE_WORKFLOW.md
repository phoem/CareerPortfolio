# LinkedIn Profile Review and Publishing Workflow

## Purpose

This manual workflow reviews Jordan Newman's LinkedIn profile against the verified CareerPortfolio knowledge base, proposes evidence-supported improvements, and publishes only changes Jordan explicitly approves.

The canonical profile URL is stored in `knowledge/Professional_Profile/README.md`.

## Invocation

Run this workflow only when Jordan explicitly asks for a LinkedIn profile review, synchronization, or approved update. It is not scheduled and must not run as an unattended GitHub Action.

LinkedIn access uses a browser session in which Jordan is already signed in, or Jordan signs in interactively when requested. Never request, capture, store, or commit LinkedIn credentials, cookies, session tokens, recovery codes, or other authentication material.

## Governing Rules

- CareerPortfolio knowledge is the factual source of truth.
- Treat the existing LinkedIn profile as content to review, not as automatically verified career evidence.
- Never invent a title, date, metric, skill, responsibility, project feature, certification, or endorsement.
- Record newly confirmed professional facts in the OKF knowledge base before using them in proposed LinkedIn wording.
- Review is read-only until Jordan explicitly approves proposed field changes.
- Approval is field-specific. Silence, general enthusiasm, or approval of one field does not authorize changes to another field.
- Never modify account security, privacy, visibility, contact preferences, job-search settings, connections, messages, recommendations, endorsements, or posts through this workflow.
- Skills may be added, removed, or reordered when supported by verified CareerPortfolio evidence and explicitly approved. Never add, remove, request, or otherwise manipulate endorsements.
- Never publish a post, notify the network, follow or unfollow an account, or send a connection request.
- If LinkedIn's current content changes after proposal generation, stop and obtain renewed approval for the affected field.
- Record every attempted or successful profile edit in `linkedin/CHANGELOG.md`.

## Phase 1: Read-Only Review

1. Read `knowledge/index.md`, `knowledge/Professional_Profile/README.md`, the three generic resumes, and relevant project and employment concepts.
2. Open the canonical LinkedIn profile in an authenticated browser session.
3. Inspect only profile sections relevant to professional positioning, including when visible:
   - headline;
   - About section;
   - current and prior experience;
   - education;
   - skills;
   - featured projects or links;
   - public contact and profile URL information.
4. Compare LinkedIn content with verified CareerPortfolio facts and identify:
   - stale or inconsistent wording;
   - missing high-value evidence;
   - unsupported or overly broad claims;
   - opportunities to improve recruiter searchability and technical positioning;
   - dates, titles, or metrics that require Jordan's confirmation.
5. Do not infer that LinkedIn-only information is correct when it conflicts with or is absent from CareerPortfolio. Ask Jordan to confirm it.

## Skills Review and Synchronization

Treat the LinkedIn Skills section as profile data that can be reviewed and updated, while treating endorsements as out of scope.

1. Compare visible LinkedIn skills with confirmed technology, domain, project, and employment knowledge.
2. Classify skills as:
   - confirmed and appropriately represented;
   - confirmed but missing;
   - duplicated, stale, misleading, or too broad;
   - unsupported and requiring Jordan's confirmation;
   - candidates for higher or lower profile priority.
3. Propose exact skill additions, removals, and ordering changes with supporting evidence.
4. Record newly confirmed skills in the appropriate OKF concept before proposing them for LinkedIn.
5. Require explicit approval for each set of skill changes.
6. After publishing, verify the visible skills and ordering without interacting with endorsements.

## Incorrect Information and Removal

When Jordan states that existing LinkedIn information is wrong or inaccurate:

1. Treat that statement as a factual correction and stop using the incorrect claim as evidence.
2. Update the relevant CareerPortfolio knowledge concept to remove, correct, or explicitly mark the contradicted information before it is reused elsewhere.
3. Propose either exact replacement wording or deletion of the affected LinkedIn field or entry.
4. Explain any consequence of deleting the entire entry instead of editing only the incorrect portion.
5. Obtain explicit publishing approval for the exact correction or deletion.

Saying that information is wrong confirms the knowledge correction, but it does not by itself authorize the external LinkedIn edit. If Jordan explicitly says to remove or replace the information on LinkedIn, that instruction may serve as field-level approval after the workflow restates the exact affected field and intended action.

## Proposal Format

Present a proposal before opening any LinkedIn edit form. For every proposed change include:

| Field | Current value | Exact proposal | Evidence | Reason | Approval status |
|---|---|---|---|---|---|

Also report:

- fields reviewed with no recommended change;
- questions or factual conflicts requiring Jordan's input;
- wording constrained by LinkedIn field limits;
- any change that may cause LinkedIn to notify the network;
- a concise priority order.

For longer fields, show the complete current value and complete exact final replacement text, not merely a description of the intended edit.

## Approval Gate

Stop after presenting the proposal. Do not edit LinkedIn until Jordan explicitly approves one of the following:

- all proposed changes;
- a named subset of fields;
- revised wording supplied or confirmed by Jordan;
- an exact deletion or replacement Jordan explicitly directs after identifying incorrect information.

Before publishing, restate the exact fields authorized and the final text that will be entered. Material wording changes made after approval require renewed approval.

## Phase 2: Approved Publishing

For each approved field, one at a time:

1. Reopen or refresh the profile and confirm the current field still matches the reviewed version.
2. Open only that field's edit interface.
3. Confirm any visible network-notification option is disabled when LinkedIn permits it, unless Jordan explicitly requests otherwise.
4. Enter the exact approved text.
5. Review the field before saving.
6. Save the change.
7. Re-read the visible profile field and verify it matches the approved text.
8. Stop immediately if the save fails, the UI behaves unexpectedly, or LinkedIn presents an additional consequential choice.
9. Append the result to `linkedin/CHANGELOG.md`, including failed or partially completed attempts.

Do not batch unverified edits. A failure in one field does not authorize alternative wording or changes elsewhere.

## Completion Report

After publishing, report:

- each field changed and its final visible text;
- each approved field not changed and why;
- verification results;
- any LinkedIn warnings or unexpected behavior;
- remaining recommendations that were not approved;
- whether CareerPortfolio knowledge or resume sources now require synchronization.

Update the relevant OKF concepts and `knowledge/log.md` when the successful LinkedIn update reflects newly confirmed professional knowledge. Do not store authentication material or unnecessary browser captures in the repository.

## Required Change Log

`linkedin/CHANGELOG.md` is an append-only audit trail. A publishing session is not complete until every attempted field change has been logged and committed.

Each entry must include all applicable information:

- ISO 8601 date and time with an explicit UTC offset;
- canonical LinkedIn profile URL;
- profile field or specific item affected;
- action: added, removed, updated, reordered, attempted, or reverted;
- exact previous visible text or state;
- exact approved intended text or state;
- final visible text or state after the attempt;
- who approved the change and the approved scope;
- success, failure, partial, or not-saved result;
- post-save verification status;
- network-notification setting observed when applicable;
- LinkedIn warning, validation message, or unexpected UI behavior;
- supporting CareerPortfolio evidence or knowledge concept;
- related CareerPortfolio commit when available;
- follow-up or rollback recommendation.

Use this entry template:

```markdown
## 2026-07-15T15:30:00-04:00 — Headline updated

- **Profile:** https://www.linkedin.com/in/example/
- **Field:** Headline
- **Action:** Updated
- **Before:** Exact prior text
- **Approved change:** Exact approved replacement
- **Final visible state:** Exact text observed after saving
- **Approval:** Profile owner approved the Headline replacement
- **Result:** Success
- **Verification:** Verified after save
- **Network notification:** Disabled / not offered / unknown
- **Evidence:** `knowledge/...`
- **Warnings or errors:** None
- **Related commit:** Pending / commit URL
- **Follow-up:** None
```

Log failures and no-save attempts honestly. If an entry is later found to be inaccurate, append a correction that references the original timestamp; do not silently rewrite or delete history.

Never log credentials, cookies, session tokens, recovery data, private messages, or other authentication and private-session material.

## Optional Review Record

When Jordan asks to preserve a review, store it under:

```text
linkedin/reviews/<YYYY-MM-DD>/
    PROPOSAL.md
    RESULT.md
```

Do not create or commit a profile snapshot or proposal record by default. The required `linkedin/CHANGELOG.md` remains mandatory for actual edit attempts; the chat proposal and completion report are sufficient for review-only sessions unless Jordan explicitly wants a durable proposal record.
