# ATS Validation Workflow

## Purpose

CareerPortfolio should evaluate a finished resume before submission for two separate concerns:

1. **ATS compatibility** — whether the document is likely to parse cleanly and expose its content to common applicant-tracking systems.
2. **Job alignment** — how well the resume's documented evidence maps to a specific job description.

No tool can produce a universal or authoritative ATS score because employers use different systems, configurations, knockout questions, recruiter workflows, and ranking models. CareerPortfolio therefore reports a transparent **heuristic readiness score** with category-level evidence and recommendations.

## Score Types

CareerPortfolio tracks two different score types:

- **Generic resume baseline score:** ATS compatibility, completeness, artifact consistency, structure, and general readability. It does not claim job-specific alignment.
- **Targeted resume readiness score:** the complete score against one specific job description, including required and preferred evidence coverage.

Do not compare these two score types directly.

## Required Inputs

- the target job description for targeted validation;
- the final Markdown resume source;
- the generated DOCX and PDF artifacts;
- relevant concepts from the `knowledge/` OKF bundle.
- the rebuilt-artifact manifest emitted by the immediately preceding generation run.

Validation is build-scoped. Automation validates only resume entries in that manifest; it must not rescan unrelated generic or targeted resumes merely because another resume was rebuilt.

## Validation Stages

### 1. Parseability and document structure

Check the actual generated artifacts, not only the Markdown source.

- text can be extracted in a logical reading order;
- contact details, headings, employers, job titles, dates, and bullets survive extraction;
- no important content is stored only in images, text boxes, headers, footers, tables, or columns that scramble reading order;
- fonts and characters render without missing glyphs;
- hyperlinks remain understandable as visible text;
- PDF and DOCX content agree with the Markdown source.

### 2. Required-information checks

- candidate name and contact information are present;
- work history includes recognizable employer, title, and date fields;
- education is present when appropriate;
- sections use conventional, descriptive headings;
- dates and locations use consistent formats;
- no placeholders, comments, unsupported claims, or stale company references remain.

### 3. Job-requirement evidence mapping

Classify job requirements as:

- **Required**
- **Preferred**
- **Contextual**

For each requirement, record:

- matching resume evidence;
- supporting OKF concept or employment record;
- strength of evidence: direct, adjacent, or missing;
- whether the wording is explicit enough for both an ATS and a human reviewer.

Missing evidence must trigger the existing gap-question workflow. Keywords may only be added when supported by confirmed experience.

### 4. Language and keyword quality

Evaluate:

- exact role and domain terminology used naturally where accurate;
- important acronyms and expanded forms when useful;
- technology names spelled consistently;
- meaningful action verbs and concrete outcomes;
- excessive repetition, keyword stuffing, vague claims, and unsupported seniority language;
- density and readability for both recruiter and technical-review audiences.

### 5. Human-quality review

A technically parseable resume can still be weak. Review:

- whether the first third communicates the strongest fit;
- whether the most relevant evidence is easy to find;
- whether bullets distinguish ownership, implementation, scale, and outcomes;
- whether the document is an appropriate length for the candidate's experience and the target role;
- whether the resume tells a coherent role-specific story.

## Heuristic Readiness Score

Score each category from 0 to 100, with the following default weighting for targeted resumes:

| Category | Weight |
|---|---:|
| Artifact parseability and structure | 25% |
| Required-information completeness | 10% |
| Required job-requirement evidence | 30% |
| Preferred job-requirement evidence | 15% |
| Language and keyword quality | 10% |
| Human readability and positioning | 10% |

Generic baseline scoring omits the job-evidence categories and renormalizes the remaining categories.

The report must always show category scores and the reasons behind them; the total alone is not sufficient.

## Suggested Interpretation

- **90-100 — Submission ready:** no critical parsing or evidence gaps; only optional polish remains.
- **80-89 — Strong:** suitable to submit after reviewing the listed improvements.
- **70-79 — Needs targeted revision:** meaningful evidence, structure, or positioning gaps remain.
- **Below 70 — Not ready:** fix critical parsing, completeness, or required-capability gaps before submission.

A high score never guarantees an interview. A low score should not be raised by inserting unsupported keywords.

## Critical-Failure Rules

Regardless of the numeric score, mark the resume **Not Ready** when any of these conditions exist:

- generated PDF or DOCX cannot be parsed reliably;
- contact information or work-history structure is missing;
- a required qualification is falsely claimed;
- unsupported metrics or technologies appear;
- the resume targets the wrong job or company;
- Markdown, DOCX, and PDF materially disagree;
- obvious placeholders, corrupted characters, or stale application content remain.

## Revision Loop

ATS validation is an iterative quality gate, not a one-time score.

Before changing a resume in response to its first validation result, commit the
initial retained baseline as described in **Per-pass commit gate** below.

When the score or disposition is below the configured submission target:

1. identify the lowest-scoring fixable categories;
2. separate presentation problems from missing knowledge and genuine qualification gaps;
3. apply one coherent set of supported improvements;
4. update the OKF knowledge base first when new facts are learned;
5. regenerate Markdown-derived DOCX and PDF artifacts;
6. rerun validation and record the score delta.
7. visually review the rebuilt artifacts;
8. commit the complete retained pass before making any further resume change.

### Per-pass commit gate

The initial baseline and every meaningful revision pass are recoverable Git
versions, not merely score-history entries.

A local or agent-driven pass is not complete until all of the following have
happened:

1. the exact Markdown source has been generated into DOCX and PDF;
2. validation has produced the current report, machine-readable result, and
   append-only history entry;
3. visual and factual review has completed;
4. the pass's scoped files have been staged and committed;
5. the commit succeeded and the remaining worktree was checked for unintended
   or unrelated changes.

The commit must include, when applicable:

- the resume Markdown source;
- the exact DOCX and PDF files listed in that pass's rebuilt-artifact manifest;
- the current ATS report and machine-readable result;
- the append-only ATS history;
- the synchronized `EVIDENCE_MAP.md`;
- application metadata or design selection changed for the pass;
- OKF concepts and `knowledge/log.md` entries that support claims introduced in
  the pass;
- a cover letter only when it was intentionally rebuilt as part of the same
  coherent application change.

Do not start the next pass until this commit exists. Do not use `--amend`,
squash, history rewriting, or a later aggregate commit to replace retained
baseline or pass commits.

Recommended commit subjects:

```text
Record <company> <role> ATS baseline (<score>)
Revise <company> <role> ATS pass <n> (<score>)
```

The ATS history's artifact hashes remain useful integrity identifiers, but they
are not a substitute for committing the files. A hash cannot reconstruct an
overwritten Markdown, DOCX, or PDF file.

In GitHub Actions, one pass may be represented by a short commit chain rather
than one commit: the user/source commit, the generated-artifact commit, and the
validation-report commit. That chain collectively preserves the pass. Do not
push the next revision pass until the preceding generation and validation jobs
have completed successfully.

### Autonomous retry limit

An agent may perform at most **three consecutive revision passes without human interaction**.

A pass includes analysis, one coherent set of edits, artifact regeneration,
rescoring, visual review, and the successful per-pass commit.

Stop before the limit when:

- the resume reaches the configured submission threshold;
- a pass produces no material improvement;
- remaining deductions require user knowledge or clarification;
- further changes would reduce readability or encourage keyword stuffing;
- further changes would require unsupported claims or factual distortion;
- the remaining issue is a genuine qualification gap;
- no responsible improvement remains.

After three autonomous passes, stop and request human direction. Do not begin a fourth pass automatically.

Meaningful human input resets the autonomous retry counter. Examples include:

- answering a gap question;
- confirming a proposed revision strategy;
- supplying new project or employment evidence;
- explicitly instructing the agent to continue.

### Required handoff report

When the loop stops below the target, provide:

- score history by pass;
- changes made in each pass;
- remaining category deductions;
- unresolved evidence or qualification gaps;
- questions requiring user input;
- prioritized recommendations;
- final recommendation: submit, revise with user input, or do not submit.

The report must be honest even when the recommendation is not to submit.

## Current Score and History

Each resume keeps a current validation result and a compact append-only history.

### Current result

Record:

- validation date;
- score type: generic baseline or targeted readiness;
- validator or scoring-model version;
- overall score and category scores;
- disposition;
- source commit or artifact version;
- job identifier or job-description hash for targeted resumes;
- link to the full report.

### History retention

Record only meaningful runs:

- the initial baseline;
- each autonomous revision pass;
- validation after meaningful human input;
- the final pre-submission result;
- later regression checks after substantial resume changes.

Do not retain duplicate runs where neither the resume, artifacts, job description, nor scoring model changed.

A score becomes stale when its resume source, generated artifacts, target job description, or scoring model changes. Stale results must be labeled and rerun before relying on them.

Every retained history entry must correspond to a recoverable Git state. For a
local pass, that is the pass commit. For an automated pass, it is the completed
source/artifact/validation commit chain. The history does not need to duplicate
the old files once Git preserves them.

### Suggested paths

Targeted resume:

```text
applications/<company>/<role>/validation/
    ATS_REPORT.md
    ATS_HISTORY.md
```

Generic resumes:

```text
generic/validation/
    <resume-name>-ATS_REPORT.md
    <resume-name>-ATS_HISTORY.md
```

## Validation Report

The report should include:

- overall readiness score;
- score type;
- category scores;
- critical failures;
- requirement-to-evidence matrix for targeted resumes;
- missing or weak evidence;
- parseability findings;
- prioritized recommendations;
- revision-pass history;
- source, artifact, job, and validator version identifiers;
- final disposition: Not Ready, Needs Revision, Strong, or Submission Ready.

Generated extraction files may be temporary when they add no lasting review value.

## Automation

`scripts/validate_resume.py` automates deterministic checks such as:

- extracting text from DOCX and PDF;
- comparing extracted content with Markdown;
- checking headings, dates, contact fields, and missing sections;
- detecting broken characters and likely reading-order problems;
- calculating transparent keyword and requirement coverage;
- generating an initial Markdown validation report;
- tracking current scores, revision-pass count, and score history;
- marking stale validation results;
- enforcing the three-pass autonomous retry limit.

Human or agent review remains required for evidence quality, relevance, truthfulness, and narrative strength.

`scripts/validate_rebuilt_artifacts.py` is the automation entry point after generation. It routes each rebuilt resume to its current validation directory, invokes the validator, and records history. Cover letters in the build manifest are intentionally skipped because ATS resume scoring does not apply to them.

The validator does not autonomously stage arbitrary repository changes because
the safe commit scope can include user-confirmed OKF evidence and application
files outside the generated manifest. The calling agent or CI workflow is
responsible for the commit gate and must preserve unrelated worktree changes.
