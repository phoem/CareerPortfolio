# Application Queue

This file tracks job applications Jordan has explicitly asked to pursue. A queued role does not receive an application package until work begins and its exact posting is captured through the resume workflow.

| Priority | Company | Role | Workflow stage | Status | Next action | Source |
|---:|---|---|---|---|---|---|
| Hold | NVIDIA | Senior Software Engineer, Networking DGX Cloud (JR2022482) | Evidence gathering | On hold at Jordan's request | Await PrimeBGP/PrimeFlow deployment details, network configuration-management evidence, and Python/Go service details | https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/US-Remote/Senior-Software-Engineer--Networking-DGX-Cloud_JR2022482?source=jobboardlinkedin |
| 2 | LM Studio | Software Engineer, AI/ML Systems | Drafting | Active | Draft after the Applications resume completes its CI baseline and review | https://lmstudio.ai/careers/ai-ml-systems-engineer |

## Workflow-stage values

- `Queued` - requested but exact posting review has not started.
- `Posting capture` - exact posting is being retrieved and preserved.
- `Gap analysis` - generic resumes and OKF evidence are being compared with the posting.
- `Evidence gathering` - material questions must be answered before accurate drafting.
- `Drafting` - application source files are being written.
- `CI baseline` - source pass is committed and generation/validation is running.
- `Revision` - a retained ATS improvement pass is underway.
- `Submission ready` - artifacts and validation passed final review.
- `On hold` - intentionally paused with the next action preserved.
- `Closed` - application was submitted, withdrawn, expired, or canceled; explain which in `Status`.

## Queue rules

- Preserve the order Jordan requested unless he reprioritizes it.
- Keep `Workflow stage`, `Status`, and `Next action` current whenever work pauses, resumes, completes a CI pass, or becomes submission-ready.
- When a role becomes active, verify that the posting is still available and capture its exact contents before selecting a resume base.
- Create a separate application package for each posting; do not share job descriptions, evidence maps, resumes, or validation history between queued roles.
- Remove a role from this queue only after its application package is created or Jordan explicitly cancels it.
