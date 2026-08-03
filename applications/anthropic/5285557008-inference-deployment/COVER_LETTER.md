# Jordan Newman

**Staff + Senior Software Engineer, Inference Deployment**

Marlboro, NJ | 347-739-4731 | phoem@mac.com | https://www.linkedin.com/in/jordan-newman-aa3b19b2/ | https://github.com/phoem

August 2, 2026

Dear Anthropic Hiring Team,

I am applying for the Staff + Senior Software Engineer, Inference Deployment role because it combines the engineering problems I have spent my career solving—high-performance request serving, distributed infrastructure, routing, reliability, observability, and production operations—with work whose societal importance is difficult to overstate.

At ISPRIME, I architected and operated a 24/7 hosting and CDN platform spanning approximately 3,000-4,000 servers across about 10 locations and carrying more than 65 Gbps of peak traffic. I personally designed and implemented PrimeHTTPD, a C/FreeBSD serving runtime deployed across approximately 200 servers and supporting more than 150,000 concurrent connections. Its architecture protected a latency-sensitive event loop from blocking storage operations through worker-process isolation, descriptor passing, shared-memory status, workload-aware dispatch, and kernel-assisted file transfer.

Operating that platform required a broader control and reliability layer. I wrote production health-check and monitoring software, including `sitecheck`, `slugd`, and `php-seclogd`, as well as networking, telemetry, deployment, packet-analysis, DNS-analysis, security, and DDoS systems. The network used multiple BGP upstreams, direct and exchange peering, private inter-PoP fiber, anycast DNS, and GeoDNS. In my current Architecture Team role, I work with Kubernetes, Terraform, Docker, CI/CD, developer tooling, and shared platform practices. I also have hands-on AWS, GCP, and Azure experience and am actively building Nexus, a local-first agent platform with model routing, health checks, circuit breakers, failover, prompt caching, and model-invocation telemetry.

I would bring Anthropic long experience owning the full operational consequences of performance-sensitive systems, from low-level runtime mechanics through global infrastructure and production response. I am especially motivated by the opportunity to apply that experience to reliable, efficient inference infrastructure that supports both customer growth and next-generation research.

Sincerely,

Jordan Newman
