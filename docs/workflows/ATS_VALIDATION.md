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

When the score or disposition is below the configured submission target:

1. identify the lowest-scoring fixable categories;
2. separate presentation problems from missing knowledge and genuine qualification gaps;
3. apply one coherent set of supported improvements;
4. update the OKF knowledge base first when new facts are learned;
5. regenerate Markdown-derived DOCX and PDF artifacts;
6. rerun validation and record the score delta.

### Autonomous retry limit

An agent may perform at most **three consecutive revision passes without human interaction**.

A pass includes analysis, one coherent set of edits, artifact regeneration, and rescoring.

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

### Suggested paths

Targeted resume:

```text
applications/<company>/<role>/validation/
    ATS_REPORT.md
    ATS_HISTORY.md
```

Existing company-specific directories may use the same `validation/` subdirectory until the broader `applications/` layout is adopted.

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

## Automation Roadmap

A future `scripts/validate_resume.py` may automate deterministic checks such as:

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