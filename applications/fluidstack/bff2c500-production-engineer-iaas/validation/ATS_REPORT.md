# ATS Readiness Report

- **Validated:** 2026-08-13T06:09:04+00:00
- **Validator:** CareerPortfolio ATS Validator v0.2.2
- **Score type:** Targeted readiness
- **Overall score:** 76/100
- **Disposition:** Needs Revision
- **Autonomous revision pass:** 0 of 3

## Category Scores

| Category | Score | Weight |
|---|---:|---:|
| Artifact parseability and structure | 100 | 25% |
| Required-information completeness | 100 | 10% |
| Required job-requirement evidence | 54 | 30% |
| Preferred job-requirement evidence | 42 | 15% |
| Language and keyword quality | 90 | 10% |
| Human readability and positioning | 97 | 10% |

## Critical Failures

- None detected.

## Artifact parseability and structure

- DOCX token coverage versus Markdown: 99.4%.
- PDF token coverage versus Markdown: 99.4%.

## Required-information completeness

- Contact details, conventional sections, and work-history dates are present.

## Required job-requirement evidence

- Adjacent: You treat toil as a bug. If something requires a human to do it twice, you build the thing that makes it not require a human. (matched: treat, toil, requires, human, build).
- Adjacent: You design APIs that age well. You've felt the pain of a leaky abstraction at scale and you don't repeat it. (matched: design, apis, age, scale).
- Adjacent: You move toward ambiguity, not away from it. You walk into the fog, build the map, and explain it to everyone else. (matched: move, toward, ambiguity, into, build, map).
- Missing: You learn at a steep slope. You reach real competence in an unfamiliar domain fast. We value this over existing expertise. (matched: real, unfamiliar).
- Adjacent: You carry a pager without flinching. You run the incident, write the postmortem, fix the systemic cause, and move on. (matched: without, incident, systemic, move).
- Adjacent: You're fluent with AI tooling. LLM APIs, MCP servers, and agentic frameworks, and you drive Claude Code, Cursor, or similar every day. (matched: ai, llm, apis, mcp, servers, agentic, frameworks, code).
- Direct: You've shipped production services that other teams depend on at scale, and you're comfortable in any language using AI coding tools. (matched: shipped, production, services, other, teams, scale, ai, coding).

## Preferred job-requirement evidence

- Direct: Distributed systems and data pipeline engineering. (matched: distributed, systems, data, pipeline, engineering.).
- Missing: Time-series observability stacks (Prometheus, Thanos, VictoriaMetrics). (matched: observability).
- Adjacent: API design and versioning at scale. (matched: api, design).
- Missing: Workflow and orchestration engines (Temporal, Cadence). (matched: workflow).
- Missing: BMC/Redfish or hardware telemetry. (matched: none).
- Direct: Go, Python, and Postgres. (matched: go, python).

## Language and keyword quality

- Qualification-language token coverage: 35.9%.

## Human readability and positioning

- 1 bullets are long enough to hinder scanning.

## Requirement-to-Evidence Matrix

| Type | Strength | Requirement | Matched terms |
|---|---|---|---|
| Required | Adjacent | You treat toil as a bug. If something requires a human to do it twice, you build the thing that makes it not require a human. | treat, toil, requires, human, build |
| Required | Adjacent | You design APIs that age well. You've felt the pain of a leaky abstraction at scale and you don't repeat it. | design, apis, age, scale |
| Required | Adjacent | You move toward ambiguity, not away from it. You walk into the fog, build the map, and explain it to everyone else. | move, toward, ambiguity, into, build, map |
| Required | Missing | You learn at a steep slope. You reach real competence in an unfamiliar domain fast. We value this over existing expertise. | real, unfamiliar |
| Required | Adjacent | You carry a pager without flinching. You run the incident, write the postmortem, fix the systemic cause, and move on. | without, incident, systemic, move |
| Required | Adjacent | You're fluent with AI tooling. LLM APIs, MCP servers, and agentic frameworks, and you drive Claude Code, Cursor, or similar every day. | ai, llm, apis, mcp, servers, agentic, frameworks, code |
| Required | Direct | You've shipped production services that other teams depend on at scale, and you're comfortable in any language using AI coding tools. | shipped, production, services, other, teams, scale, ai, coding, tools. |
| Preferred | Direct | Distributed systems and data pipeline engineering. | distributed, systems, data, pipeline, engineering. |
| Preferred | Missing | Time-series observability stacks (Prometheus, Thanos, VictoriaMetrics). | observability |
| Preferred | Adjacent | API design and versioning at scale. | api, design |
| Preferred | Missing | Workflow and orchestration engines (Temporal, Cadence). | workflow |
| Preferred | Missing | BMC/Redfish or hardware telemetry. | None |
| Preferred | Direct | Go, Python, and Postgres. | go, python |

## Artifact Versions

- `resume`: `183f429f66907881a56d1a5e1d404568cc754b357ee6199d8839d73883fa9916`
- `docx`: `97bb8edc4c240ebbecca47f21024d45fb750a08064038e539e3b99a0aae11900`
- `pdf`: `85f2738f4df7cb6c14966b3a13ded0f8f327898f0c5fad8231063f7d15d29b16`
- `job`: `519df57152a39adc8c59e4217326bcea0146ac3c1570a26e06189554a3dcef03`

## Recommended Next Action

- Revise the lowest-scoring fixable categories, regenerate artifacts, and rerun validation. Stop after three autonomous passes or earlier when a stop condition is reached.
