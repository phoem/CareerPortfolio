# CareerPortfolio Starter Guide

This guide explains how another person can create a new CareerPortfolio without copying Jordan Newman's private career data.

## Recommended Starter Files

Copy these repository-level files and directories:

```text
README.md
AGENTS.md
docs/
  workflows/
    RESUME_WORKFLOW.md
    ATS_VALIDATION.md
  OKF_PORTFOLIO.md
  STARTER_GUIDE.md
  ROADMAP.md
  decisions/
    README.md
designs/
  README.md
  default.json
  classic-ats/
    design.json
scripts/
  generate_resume_artifacts.py
  validate_resume.py
  record_ats_history.py
.github/workflows/
  generate-resume-artifacts.yml
  validate-resumes.yml
```

Create these empty or template-backed directories:

```text
knowledge/
  index.md
  log.md
generic/
applications/
```

Do not copy another person's project concepts, resumes, metrics, contact details, or company-specific application materials unless they are being used only as examples and are fully replaced.

## Application Package Structure

Create a separate directory for every individual posting:

```text
applications/
  example-company/
    REQ123-example-role/
      APPLICATION.json
      JOB_DESCRIPTION.md
      Example_Resume.md
      Example_Cover_Letter.md
      DESIGN.json
      validation/
```

A second role at the same company gets a sibling posting directory. Never overwrite or combine job descriptions merely because the employer is the same.

`APPLICATION.json` identifies the posting and the source artifacts:

```json
{
  "company": "Example Company",
  "role": "Example Role",
  "requisition_id": "REQ123",
  "slug": "REQ123-example-role",
  "job_description": "JOB_DESCRIPTION.md",
  "artifacts": [
    {"type": "resume", "source": "Example_Resume.md"},
    {"type": "cover_letter", "source": "Example_Cover_Letter.md"}
  ]
}
```

## Resume Design Selection

The repository default is stored in `designs/default.json`.

For one application package:

- add `DESIGN.json` to use a design for all future rebuilds of that posting;
- add `DESIGN_NEXT.json` to use a design only for the next successful build.

`DESIGN_NEXT.json` takes precedence and is removed after generation. See `designs/README.md`.

## Minimal Knowledge Bundle

`knowledge/index.md` should declare the OKF version and list available concepts:

```markdown
---
okf_version: "0.1"
---

# Career Knowledge Base

# Projects

* [Example Project](Example_Project/README.md) - Short description.
```

`knowledge/log.md` should start with a dated initialization entry:

```markdown
# Knowledge Base Update Log

## YYYY-MM-DD

* **Initialization**: Created the CareerPortfolio knowledge bundle.
```

Each concept is a Markdown file with YAML frontmatter:

```markdown
---
type: Software Project
title: Example Project
description: One-sentence summary.
tags: [example]
status: partial
owner: Person Name
evidence_status: confirmed
---

# Example Project

## Summary

Describe only confirmed facts.

## Personal Ownership

Describe what the person personally designed, implemented, operated, or led.

## Open Questions

- Details worth asking about later.
```

## What the Workflow Creates Automatically

The resume workflow does not silently invent or create the entire repository structure. The foundational directories and core instruction files should exist before work begins.

After initialization, an agent may create new items as needed:

- new OKF concept directories and Markdown files under `knowledge/`;
- new entries in `knowledge/index.md`;
- dated entries in `knowledge/log.md`;
- new application packages under `applications/<company>/<posting>/`;
- Markdown resume and cover-letter sources;
- generated DOCX and PDF artifacts;
- ATS validation reports and score histories;
- persistent or one-build design selections.

This deliberate initialization prevents accidental assumptions about resume types, directory names, personal data, or career goals.

## Initial Interview

A new CareerPortfolio should begin by gathering:

1. contact and location information;
2. current and previous roles with dates;
3. preferred target roles;
4. technologies and domains with actual experience;
5. major projects and personal ownership;
6. production scale and verified metrics;
7. leadership, architecture, and operational responsibilities;
8. public links and private-work availability notes;
9. education and certifications;
10. work-location and travel preferences.

Capture confirmed project knowledge first, then build the canonical generic resumes from that knowledge.

## Recommended First Milestone

A useful initial repository contains:

- one populated professional-profile concept;
- three to five project concepts;
- one metrics concept;
- one technologies concept;
- at least one canonical generic resume;
- the workflow, application-package, and design documentation;
- no unsupported claims.
