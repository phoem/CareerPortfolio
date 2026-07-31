# Jordan Newman

**Software Engineer, Research Infrastructure**

Marlboro, NJ | 347-739-4731 | phoem@mac.com | https://www.linkedin.com/in/jordan-newman-aa3b19b2/ | https://github.com/phoem

July 31, 2026

Dear Anthropic Hiring Team,

I am applying for the Software Engineer, Research Infrastructure role because it brings together the work I do best: taking complex infrastructure from first-principles architecture through hands-on implementation, scaling it under real production load, and building platforms and tools that make other engineers more effective.

At ISPRIME, I architected and operated a 24/7 hosting and CDN platform spanning approximately 3,000-4,000 servers across about 10 locations and carrying more than 65 Gbps of peak traffic. I personally designed and implemented PrimeHTTPD, a high-concurrency HTTP/CDN runtime in C for FreeBSD that was deployed across approximately 200 production servers and supported more than 150,000 concurrent connections.

PrimeHTTPD kept its latency-sensitive networking path in one event-driven process built around `kqueue`, non-blocking sockets, HTTP accept filtering, and kernel-assisted `sendfile()` transfers. Potentially blocking file opens and disk-backed sends were delegated to configurable I/O workers through `sendmsg()` descriptor passing. Shared `mmap()` state exposed worker activity and supported least-busy-worker assignment. I also implemented caching, authentication integration, request rewriting, HTTP protocol features, and live configuration reloads.

The surrounding platform required more than a fast serving runtime. I built monitoring, telemetry, deployment, authentication, packet and DNS analysis, DDoS detection and mitigation, security, and infrastructure-management systems for customer-facing operations. That work demanded architectural judgment across operating systems, networking, storage I/O, reliability, observability, and changing production constraints.

In my current role at Advantive, I serve on the Architecture Team and collaborate on technical decisions, engineering standards, shared platforms, developer tooling, libraries, and documentation. My work includes Terraform, Kubernetes, Docker, Azure DevOps, CI/CD, security scanning, and AI-assisted engineering workflows.

I would bring Anthropic proven depth in designing and operating demanding systems, the ability to move comfortably between low-level implementation and platform architecture, and a long record of owning the operational consequences of engineering decisions. I would welcome the opportunity to apply that experience to infrastructure that shortens research feedback loops and remains reliable as Anthropic's workloads evolve.

Sincerely,

Jordan Newman
