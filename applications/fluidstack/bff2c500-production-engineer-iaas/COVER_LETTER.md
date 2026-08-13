# Jordan Newman

**Production Engineer, IaaS**

Marlboro, NJ | 347-739-4731 | phoem@mac.com | https://www.linkedin.com/in/jordan-newman-aa3b19b2/ | https://github.com/phoem

August 13, 2026

Dear Fluidstack Hiring Team,

I am applying for the Production Engineer, IaaS role because it closely matches the work I have done throughout my career: making large production systems observable, replacing repeated operational work with durable tooling, and owning infrastructure from an unclear problem through architecture, implementation, and operation.

At ISPRIME, I architected and operated a 24/7 hosting and CDN platform spanning approximately 3,000-4,000 servers across about 10 locations and carrying more than 65 Gbps of peak traffic. I personally built its health-check, monitoring, telemetry, deployment, authentication, networking, security, and infrastructure-management software. That included `sitecheck`, `slugd`, and `php-seclogd`; a modular NetFlow collection pipeline; packet- and DNS-analysis tools; and DDoS detection and mitigation systems.

I also designed and implemented PrimeHTTPD, a high-concurrency C/FreeBSD serving runtime deployed across approximately 200 servers and supporting more than 150,000 concurrent connections. Its architecture combined a single `kqueue` networking core with Unix descriptor passing, shared-memory worker telemetry, workload-aware dispatch, and non-blocking `sendfile()` behavior. The work required treating operational visibility, failure diagnosis, and reliable control as core platform capabilities rather than afterthoughts.

In my current role at Advantive, I serve on the Architecture Team and contribute to APIs and integrations, engineering standards, shared libraries, platform direction, and developer tooling. I support about 12 teams with reusable Azure Pipelines, templates, deployment gates, and self-hosted runners that reduce manual work and enable quicker releases. My work also includes Kubernetes, Docker, Terraform, security scanning, and AI-assisted engineering workflows.

I am currently building Nexus, a local-first agentic control plane with LLM routing, MCP integrations, declarative workflows, permissioned tools, task-state transitions, approvals, and audit records. That project reflects the same engineering approach I would bring to Fluidstack: stable interfaces, explicit state, strong operational visibility, and automation that other engineers can depend on.

Fluidstack's combination of hyperscale infrastructure, observability, control-plane engineering, and extreme end-to-end ownership is particularly compelling to me. I am willing and able to work in person in New York City and would welcome the opportunity to help make Fluidstack's fleet legible, reliable, and easier for every team to operate.

Sincerely,

Jordan Newman
