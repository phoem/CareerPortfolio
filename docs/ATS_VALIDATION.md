# ATS Validation Workflow

## Purpose

CareerPortfolio should evaluate a finished resume before submission for two separate concerns:

1. **ATS compatibility** — whether the document is likely to parse cleanly and expose its content to common applicant-tracking systems.
2. **Job alignment** — how well the resume's documented evidence maps to a specific job description.

No tool can produce a universal or authoritative ATS score because employers use different systems, configurations, knockout questions, recruiter workflows, and ranking models. CareerPortfolio therefore reports a transparent **heuristic readiness score** with category-level evidence and recommendations.

## Required Inputs

- the target job description;
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

Score each category from 0 to 100, with the following default weighting:

| Category | Weight |
|---|---:|
| Artifact parseability and structure | 25% |
| Required-information completeness | 10% |
| Required job-requirement evidence | 30% |
| Preferred job-requirement evidence | 15% |
| Language and keyword quality | 10% |
| Human readability and positioning | 10% |

The overall readiness score is the weighted total. The report must always show category scores and the reasons behind them; the total alone is not sufficient.

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

## Validation Report

Each targeted application should eventually be able to include an optional report such as:

```text
applications/<company>/<role>/validation/
    ATS_REPORT.md
    extracted-pdf.txt
    extracted-docx.txt
```

The report should include:

- overall readiness score;
- category scores;
- critical failures;
- requirement-to-evidence matrix;
- missing or weak evidence;
- parseability findings;
- prioritized recommendations;
- final disposition: Not Ready, Needs Revision, Strong, or Submission Ready.

Generated extraction files may be temporary when they add no lasting review value.

## Automation Roadmap

A future `scripts/validate_resume.py` may automate deterministic checks such as:

- extracting text from DOCX and PDF;
- comparing extracted content with Markdown;
- checking headings, dates, contact fields, and missing sections;
- detecting broken characters and likely reading-order problems;
- calculating transparent keyword and requirement coverage;
- generating an initial Markdown validation report.

Human or agent review remains required for evidence quality, relevance, truthfulness, and narrative strength.
