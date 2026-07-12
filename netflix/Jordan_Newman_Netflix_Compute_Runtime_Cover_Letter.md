# Jordan Newman - Netflix Cover Letter

**Application: Distributed Systems Engineer (L5 + L6), Compute Runtime**

Jordan Newman  
Marlboro, NJ  
347-739-4731  
phoem@mac.com  

Dear Netflix Hiring Team,

I am applying for the Distributed Systems Engineer, Compute Runtime position. My strongest work has been at the boundary between systems software and large-scale production infrastructure: building runtimes, networking software, kernel modules, operational tooling, and reliability systems that had to perform under real traffic and failure conditions.

At ISPrime, I architected and operated infrastructure spanning approximately 3,000-4,000 servers across 10 locations with more than 65 Gbps of peak traffic. I designed and built PrimeHTTPD, a high-performance, non-blocking HTTP/CDN server in C for FreeBSD. Its event-driven architecture used kqueue, persistent connections, sendfile(), SF_NODISKIO, O_NONBLOCK, TCP_NODELAY, TCP_NOPUSH, accept_filter_http, and dedicated I/O workers so disk activity would not block latency-sensitive network processing. PrimeHTTPD was deployed across approximately 200 production servers and supported more than 150,000 concurrent connections.

I also built the systems around that runtime: deployment and operational tooling, monitoring, telemetry, authentication, traffic analysis, DNS monitoring, and DDoS detection and mitigation. My FreeBSD work included VirtualDir, a production kernel module that transparently virtualized filesystem paths by intercepting filesystem-related system calls, plus its runtime management tool. More recently, I have implemented Docker, Kubernetes, Terraform, Azure DevOps, CI/CD, and security-scanning practices across engineering teams.

The Compute Runtime role is compelling because it aligns with the work I have consistently enjoyed most: designing low-level software abstractions, understanding operating-system behavior, removing bottlenecks, separating blocking from latency-sensitive execution, and operating systems at meaningful scale. I would bring both hands-on systems depth and the perspective of someone who has owned architecture, implementation, and 24/7 production outcomes.

Thank you for considering my application.

Sincerely,

Jordan Newman
