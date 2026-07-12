# CareerPortfolio Roadmap

This roadmap records useful future ideas without committing the repository to premature structure or implementation. Items should move into active work only when they solve a real need.

## Current Foundation

- Google Cloud Open Knowledge Format (OKF) knowledge bundle.
- Three canonical generic resumes.
- Targeted application packages based on real job listings.
- Resume tailoring and knowledge-capture workflow.
- Starter guide for creating a new CareerPortfolio.
- Architecture Decision Records under `docs/decisions/`.
- Generated Markdown, DOCX, and PDF application artifacts.
- Documented ATS readiness and final-resume validation workflow.

## Near-Term Enhancements

These are accepted ideas that directly improve current resume and application work.

- Complete the shared verified metrics catalog.
- Complete the shared confirmed technology-experience catalog.
- Add a resume and artifact style guide.
- Add a stable professional-profile knowledge concept.
- Implement `scripts/validate_resume.py` for deterministic ATS-readiness checks and Markdown report generation.
- Validate the actual generated PDF and DOCX artifacts, not only Markdown sources.
- Continue expanding project concepts only as real job requirements expose useful gaps.
- Add validation checks for OKF conformance, broken links, duplicated metrics, and inconsistent resume claims.

## Future Capabilities

Add these when a real application, interview, promotion, or public-profile need justifies them.

- Interview preparation workflow.
- STAR-format interview stories.
- Role- and company-specific interview packets.
- LinkedIn profile generation and synchronization.
- Recruiter-facing professional profile.
- Promotion packets and performance-review evidence.
- Executive and conference biographies.
- Consulting capability statements and project case studies.
- Public portfolio website generation.
- Architecture diagrams for flagship projects.
- Career timeline visualization.
- GitHub Actions quality gate for ATS readiness, artifact consistency, and OKF validation.

## Parking Lot

Useful ideas that do not yet justify implementation.

- Speaking-engagement tracking.
- Conference-talk proposals and supporting materials.
- Publications and technical article catalog.
- Patent and invention tracking.
- Awards and recognition catalog.
- Mentoring and coaching evidence.
- Open-source contribution summaries.
- Presentations and slide-deck generation.
- Professional references and recommendation tracking.
- Automated job-listing evidence maps and fit scoring.
- Automated portfolio completeness and interview-readiness scoring.
- Calibration against multiple third-party ATS scanners when useful and legally/technically practical.

## Promotion Criteria

An item should move from the roadmap into implementation when one or more of the following is true:

- a real job listing requires it;
- the same manual work has been repeated more than once;
- missing structure is causing contradictory or lost information;
- the capability materially improves application or interview quality;
- Jordan explicitly chooses to prioritize it.

## Governing Principle

Do not add directories, schemas, or automation merely because they may be useful someday. Record the idea here first, then implement it when it solves a demonstrated problem.
