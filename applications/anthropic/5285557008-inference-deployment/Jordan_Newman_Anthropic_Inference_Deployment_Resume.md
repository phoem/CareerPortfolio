# Jordan Newman

**Senior Software Engineer | Distributed Systems, Request Routing, Production Infrastructure**

Marlboro, NJ | 347-739-4731 | phoem@mac.com | https://www.linkedin.com/in/jordan-newman-aa3b19b2/ | https://github.com/phoem  
Willing and able to work in Anthropic's New York City office

## Summary

Senior software and infrastructure engineer with 20+ years designing, building, and operating performance-sensitive distributed systems. Architected 24/7 hosting and CDN infrastructure spanning approximately 3,000-4,000 servers, about 10 locations, and more than 65 Gbps of peak traffic. Personally built its high-concurrency C/FreeBSD serving runtime, production health-check and monitoring systems, and substantial networking and operational software. Results-oriented and impact-focused, with the flexibility to take responsibility outside a narrowly defined job description when the work demands it. Motivated by technical excellence that drives business results and enables research breakthroughs; eager to deepen machine-learning systems and infrastructure expertise while contributing to work whose societal impact matters.

## Core Capabilities

- **Distributed infrastructure:** High-performance distributed systems, request serving, load balancing, traffic management, fleet operations, reliability, observability, performance tuning
- **Systems engineering:** C, C++, Python, Rust, Go, FreeBSD, Linux, `kqueue`, shared memory, inter-process communication, non-blocking I/O, `sendfile()`, GDB, Valgrind, Linux perf
- **Networking:** TCP/IP, HTTP, DNS, BGP4, anycast DNS, GeoDNS, CDN architecture, direct and exchange peering, NetFlow, SNMP, libpcap, DDoS mitigation
- **Platform and cloud:** Kubernetes, Docker, Terraform, CI/CD, Azure DevOps; hands-on AWS, Google Cloud Platform (GCP), and Microsoft Azure experience
- **AI and ML systems:** LM Studio, llama.cpp, Ollama, LM Studio Bionic; familiarity with CUDA, MLX, TensorFlow, and Hugging Face Transformers

## Selected Impact

- Architected and operated a customer-facing hosting and CDN platform spanning approximately 3,000-4,000 servers across about 10 locations and carrying more than 65 Gbps of peak traffic.
- Designed and implemented PrimeHTTPD, a high-performance HTTP/CDN runtime in C for FreeBSD deployed across approximately 200 servers and supporting more than 150,000 concurrent connections.
- Kept latency-sensitive request processing non-blocking through a single-process `kqueue` event loop, configurable I/O workers, and zero-copy `sendfile()` transfers.
- Implemented Unix-domain `sendmsg()` descriptor passing, shared `mmap()` worker state, and least-busy-worker dispatch for blocking work.
- Built production health-check and monitoring software—including `sitecheck`, `slugd`, and `php-seclogd`—plus telemetry, deployment, security, packet-analysis, DNS-analysis, and DDoS systems for 24/7 operations.
- Helped design, deploy, migrate, and operate multi-datacenter and point-of-presence infrastructure using multi-provider BGP, direct and exchange peering, private inter-PoP fiber, anycast DNS, and GeoDNS.

## Relevant Engineering

### Request Serving, Routing, and Observability

- Implemented PrimeHTTPD descriptor and gzip caches, persistent connections, chunked encoding, ETags, conditional requests, authentication integration, request rewriting, and hot configuration reload around its event-driven serving core.
- Designed and programmed PrimeBGP, a passive BGP4 speaker that accepted peering sessions, processed route updates, and maintained learned prefixes in an in-memory red-black tree for policy-based rerouting.
- Built PrimeFlow, a NetFlow v5 collector daemon with a modular processing pipeline and companion packet-capture flow generator; also developed SNMP-based monitoring utilities.
- Created PrimeDump and PrimeDNSTop for real-time packet and DNS analysis, production troubleshooting, abnormal-activity detection, and DDoS investigation.
- Profiled and optimized CPU-intensive systems software using GDB, Valgrind, Linux perf, and other native debugging and performance tools.

### Current AI and Platform Engineering

- Designing and building Nexus, a local-first agentic control plane with declarative multi-agent workflows, human approvals, default-deny tool permissions, auditable execution, and layered knowledge.
- Implemented deterministic model-routing profiles with provider health checks, circuit breakers, budget-aware selection, failover policies, prompt caching, and usage, latency, retry, error, and cost telemetry.
- Built React/Tailwind and Tauri interfaces with live event streams, approval workflows, routing simulation, AI-usage statistics, keychain-backed secrets, and local process supervision.
- Contributed a merged Rust Azure Key Vault provider to `cachix/secretspec`, covering multiple authentication modes, validation, integration tests, sovereign-cloud support, documentation, and maintainer-review fixes.

## Professional Experience

### Advantive — Senior Development Specialist, APIs and Integrations
*Remote / Tampa Bay, FL | June 2022 - Present*

- Serve on the Architecture Team, collaborating on technical decisions, engineering standards, platform direction, shared libraries, documentation, and developer tooling across engineering teams.
- Implement and improve Kubernetes, Docker, Terraform, Azure DevOps, CI/CD, security-scanning, and AI-assisted engineering workflows supporting shared platform delivery.

### DDI System — Senior Development Specialist
*Manalapan, NJ | October 2021 - July 2022*

- Developed primarily C# desktop applications and UniVerse database connectivity; added OAuth 2.0 email support plus SellerCloud and product-catalog integrations.

### ISPRIME — Chief Executive Officer
*Weehawken, NJ | March 2018 - December 2019*

- Led datacenter modernization, operational restructuring, and improvements to internally developed monitoring, security, and infrastructure platforms.

### ISPRIME — Owner and CIO
*Weehawken, NJ | January 2001 - December 2014*

- Held architectural and operational responsibility for a 24/7 hosting and CDN platform spanning approximately 3,000-4,000 servers, about 10 locations, multiple datacenters, and more than 65 Gbps of peak traffic.
- Personally architected and implemented PrimeHTTPD from first-principles design through production deployment, combining high-concurrency request serving, workload-aware worker dispatch, caching, authentication, and operational controls.
- Built production networking, monitoring, health-check, telemetry, authentication, deployment, infrastructure-management, and DDoS defense software in response to real operational requirements.
- Developed production FreeBSD kernel modules for transparent filesystem virtualization, execution monitoring, system protection, telemetry, and filesystem-performance instrumentation.
- Created internal training documentation, trained the majority of employees over the years, and mentored two beginners over several years into technical experts and company leaders.

### Earlier Software and Systems Experience

- **DDI System — Computer Programmer** | April 2017 - March 2018: Built ERP integrations and automated order, catalog, image, safety-data, SFTP, supplier, SellerCloud, and MultiValue/UniVerse workflows.
- **Too Much Media — Computer Programmer** | January 2016 - April 2017: Developed real-time browser chat integrated with ticketing and implemented OAuth 2.0 authorization.
- **MFCXY — Computer Programmer** | December 2014 - September 2015: Developed backend and Windows-client features plus cross-platform database-migration middleware.
- **AJPM — Programmer / Owner** | November 2012 - December 2013: Built software for purchasing, inventory, repair, resale, and financial workflows.
- **FatWallet.com — Systems Administrator** | December 2000 - June 2001: Rebuilt production infrastructure to resolve performance and stability issues without customer-facing downtime and created automated availability and health alerting.

## Education

**Brookdale Community College** — Computer Science coursework; left during the first semester to pursue ISPRIME full-time during rapid company growth.
