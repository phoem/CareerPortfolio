# Jordan Newman

**Software Engineer, Compute Infrastructure**

Marlboro, NJ | 347-739-4731 | phoem@mac.com | https://github.com/phoem

July 30, 2026

Dear OpenAI Hiring Team,

I am applying for the Software Engineer, Compute Infrastructure role because it closely matches the work I have spent much of my career doing: building low-level systems software, operating large production infrastructure, diagnosing difficult failures across software and networking layers, and turning those lessons into more reliable platforms and better tooling.

At ISPrime, I architected and operated hosting and CDN infrastructure spanning approximately 3,000–4,000 servers across about 10 locations and carrying more than 65 Gbps of peak traffic. I also designed and implemented PrimeHTTPD, a high-concurrency HTTP/CDN runtime in C for FreeBSD that was deployed across approximately 200 production servers and supported more than 150,000 concurrent connections.

PrimeHTTPD kept its latency-sensitive networking core in one main event-driven process using `kqueue`, HTTP accept filtering, non-blocking sockets, persistent connections, and kernel-assisted `sendfile()` transfers. Potentially blocking file opens and disk-backed sends were delegated to configurable I/O workers. The main process dispatched work and transferred file and client-socket descriptors through `sendmsg()`, while shared `mmap()` state exposed worker activity and enabled least-busy-worker assignment. I also built file-descriptor and gzip caches, configuration reloads, authentication integration, rewrite support, and HTTP features including chunked encoding, ETags, and conditional requests.

Beyond the serving runtime, I built FreeBSD kernel modules, packet and DNS analysis tools, DDoS detection and mitigation systems, monitoring, telemetry, deployment automation, authentication services, and operational software used in 24/7 production environments. This work required careful reasoning across operating systems, networking protocols, storage behavior, performance, reliability, and real operational constraints.

In my current role at Advantive, I work across architecture and engineering enablement, including Docker, Kubernetes, Terraform, Azure DevOps, CI/CD, security scanning, shared libraries, technical standards, documentation, and AI-assisted engineering workflows. I enjoy building leverage for other engineers and creating durable improvements rather than isolated fixes.

My strongest fit within OpenAI Compute Infrastructure is in low-level systems, networking, reliability, observability, compute foundations, and infrastructure tooling. I bring deep systems judgment, proven production ownership, and the ability to move from kernel and runtime behavior through network operations and developer-facing platform improvements.

I would welcome the opportunity to help OpenAI make enormous compute systems faster, more reliable, easier to diagnose, and easier for researchers and product teams to use.

Sincerely,

Jordan Newman
