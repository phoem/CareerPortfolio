# Gap Analysis — Fluidstack Production Engineer, IaaS

## Strong direct alignment

- Built and operated 24/7 production infrastructure spanning approximately 3,000-4,000 servers, about 10 locations, and more than 65 Gbps of peak traffic.
- Personally designed and implemented production health-check, monitoring, telemetry, NetFlow, packet-analysis, DNS-analysis, deployment, and infrastructure-management software.
- Designed distributed systems and a high-concurrency serving runtime deployed across approximately 200 servers and supporting more than 150,000 concurrent connections.
- Supports about 12 teams with reusable Azure Pipelines, templates, deployment gates, and self-hosted runners that reduce manual work and enable quicker releases.
- Professional Kubernetes workflow experience and hands-on architecture work spanning APIs, integrations, shared tooling, standards, and platform direction.
- Builds Nexus, an agentic control plane using MCP integrations, model routing, permissioned tools, auditable state transitions, and declarative multi-agent workflows.
- More than 15 years leading major ISPRIME engineering projects, often taking an unclear problem through architecture, hands-on implementation, and production operation.

## Adjacent or bounded alignment

- The production-monitoring evidence is strong, but exact monitored signals, data volume, alerting, retention, and correlation behavior are not documented.
- Infrastructure API design is supported by current architecture/API/integration work, but stable versioning mechanisms and consumer scale for a particular API are not documented.
- Kubernetes experience concerns production engineering workflows; it does not establish implementation of Kubernetes control-plane internals.
- Datacenter, DNS, deployment, and provisioning-adjacent experience does not establish ZTP, DHCP, artifact-distribution, or GPU/XPU-generation integration.
- 24/7 operational responsibility and attack response are documented; pager rotation, formal incident command, and postmortem authorship are not.
- Go and long-term periodic Python experience are documented. Postgres is not.

## Genuine gaps

- No documented GPU/XPU, BMC, or Redfish telemetry experience.
- No documented Prometheus, Thanos, or VictoriaMetrics experience.
- No documented Temporal or Cadence experience.
- No documented ZTP or DHCP implementation experience.
- No documented formal fleet-state source of truth, CMDB, SLO ownership, or site lifecycle state machine.
- No documented Postgres experience.

## Drafting boundary

Lead with verified large-fleet operations, observability and health-check engineering, distributed systems, API/platform architecture, Kubernetes workflows, AI tooling, automation, and end-to-end ownership. Do not insert the employer's missing named technologies as implied equivalents or claim GPU-specific experience.
