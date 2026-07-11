# AGENTS.md

## Purpose

This repository is a living resume, project-knowledge, and application-material system for Jordan Newman.

Agents working in this repository must preserve factual accuracy, avoid inventing experience, and tailor each resume to the target role using only documented information or facts confirmed directly by Jordan.

## Source-of-Truth Hierarchy

1. `portfolio/` project files are the authoritative source for project-specific facts.
2. `generic/` contains the three canonical reusable resumes:
   - Senior Software Engineer
   - Software Architect
   - Backend / Infrastructure Engineer
3. Company-specific directories contain targeted application packages derived from the best-fitting generic resume and the portfolio.
4. `docs/RESUME_WORKFLOW.md` defines the detailed operating process.

## Required Behavior

- Read the job description before selecting a resume base.
- Compare the role requirements against all three generic resumes.
- Select the closest base resume rather than blindly reusing the most recent one.
- Review relevant project files in `portfolio/` before drafting claims or bullets.
- Never invent technologies, metrics, responsibilities, dates, outcomes, or project features.
- When a role needs evidence that is not documented, ask Jordan whether he has worked on a project involving the missing capability.
- If Jordan confirms relevant experience, gather only the details needed to document it accurately, then update the appropriate portfolio file before using it in a resume.
- Leave unknown fields out rather than filling them with assumptions.
- Prefer concrete scale, architecture, implementation details, and measured outcomes when documented.
- Tailor technical depth to the audience: recruiter, ATS, hiring manager, systems engineer, or architect.
- Keep the three generic resumes broadly reusable while selectively improving each with the strongest relevant project descriptions.
- Keep company-specific resumes tightly aligned to the target posting.

## Project Knowledge Capture

When Jordan provides new information about a project:

1. Update the corresponding project file under `portfolio/`.
2. Record factual implementation details, scale, technologies, outcomes, and operational context.
3. Preserve uncertainty explicitly where appropriate.
4. Add resume-ready variants only when they are supported by the documented facts.
5. Do not require every project file to have every possible section; grow documentation incrementally as relevant information becomes available.

## Resume Generation

- Markdown is the editable source format.
- DOCX and PDF are generated deliverables and must remain consistent with the Markdown source.
- Preserve ATS-safe structure in ATS variants.
- Avoid dense keyword stuffing or unsupported claims.
- Use role-specific wording while keeping the underlying facts consistent across variants.

## Repository Changes

- Prefer a dedicated branch and pull request for meaningful updates.
- Use clear commit messages that describe the resume, portfolio, or workflow change.
- Do not reorganize or rename existing files without a concrete benefit and corresponding README update.
