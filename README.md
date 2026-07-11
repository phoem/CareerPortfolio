# Jordan Newman Resume Package

This repository stores canonical resumes, targeted application materials, and a growing project-knowledge portfolio used to create accurate role-specific resumes and cover letters.

## Current Package

### Starlink

| Document | Markdown | DOCX | PDF |
|---|---:|---:|---:|
| ATS Resume | `starlink/Jordan_Newman_Starlink_ATS_Resume.md` | `starlink/Jordan_Newman_Starlink_ATS_Resume.docx` | `starlink/Jordan_Newman_Starlink_ATS_Resume.pdf` |
| Recruiter 2-Page Resume | `starlink/Jordan_Newman_Starlink_Recruiter_2Page_Resume.md` | `starlink/Jordan_Newman_Starlink_Recruiter_2Page_Resume.docx` | `starlink/Jordan_Newman_Starlink_Recruiter_2Page_Resume.pdf` |
| Cover Letter | `starlink/Jordan_Newman_Starlink_Cover_Letter.md` | `starlink/Jordan_Newman_Starlink_Cover_Letter.docx` | `starlink/Jordan_Newman_Starlink_Cover_Letter.pdf` |

### Generic

The three generic resumes are the canonical reusable bases for future applications.

| Document | Markdown | DOCX | PDF |
|---|---:|---:|---:|
| Senior Software Engineer Resume | `generic/Jordan_Newman_Generic_Senior_Software_Engineer_Resume.md` | `generic/Jordan_Newman_Generic_Senior_Software_Engineer_Resume.docx` | `generic/Jordan_Newman_Generic_Senior_Software_Engineer_Resume.pdf` |
| Software Architect Resume | `generic/Jordan_Newman_Generic_Software_Architect_Resume.md` | `generic/Jordan_Newman_Generic_Software_Architect_Resume.docx` | `generic/Jordan_Newman_Generic_Software_Architect_Resume.pdf` |
| Backend / Infrastructure Resume | `generic/Jordan_Newman_Generic_Backend_Infrastructure_Resume.md` | `generic/Jordan_Newman_Generic_Backend_Infrastructure_Resume.docx` | `generic/Jordan_Newman_Generic_Backend_Infrastructure_Resume.pdf` |

## Project Portfolio

The `portfolio/` directory is the source of truth for documented project details used across resumes and interview preparation. It grows incrementally as new facts become relevant and are confirmed.

Current project knowledge:

- `portfolio/PrimeHTTPD/README.md` — high-performance FreeBSD HTTP/CDN server and platform context
- `portfolio/VirtualDir/README.md` — FreeBSD kernel filesystem-path virtualization module and `vdcli` management tool

Unknown information is deliberately omitted rather than guessed.

## Resume Workflow

- `AGENTS.md` contains concise repository-level instructions for AI and coding agents.
- `docs/RESUME_WORKFLOW.md` documents the detailed resume-selection, evidence-mapping, gap-question, and project-knowledge process.

When tailoring a resume, the workflow compares the posting against all three generic resumes, selects the strongest base, uses documented portfolio evidence, and asks targeted questions only when meaningful gaps remain.

## Positioning

Core positioning across the package:

> Systems software engineer with experience in kernel development, operating systems, networking, security, embedded firmware, and large-scale infrastructure.

The Starlink materials emphasize embedded software, FreeBSD/Linux systems programming, kernel modules, C networking software, AVR firmware, bootloaders, operating-system work, DDoS mitigation, telemetry, and large-scale infrastructure.

The generic materials provide reusable versions for Senior Software Engineer, Software Architect, and Backend / Infrastructure Engineer roles. Each version selectively emphasizes the same verified experience according to its target audience.

## File Format Notes

- Markdown files are the source/editable GitHub-native versions.
- DOCX files are editable word-processor versions for manual customization.
- PDF files are application-ready exports.
- Generated DOCX and PDF files should remain consistent with their Markdown source.
