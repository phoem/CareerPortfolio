# Evidence Map — OpenAI Software Engineer, Compute Infrastructure

## Overall Positioning

Jordan is a strong match for the posting's low-level systems, large-scale networking, reliability, observability, production ownership, infrastructure tooling, and developer-platform dimensions. The application should be candid that his strongest evidence comes from CPU/network/storage-oriented infrastructure rather than direct production GPU, RDMA, or NCCL work.

## Requirement-to-Evidence Map

| OpenAI signal | Portfolio evidence | Strength | Resume use |
|---|---|---:|---|
| Production infrastructure systems | Architected and operated hosting/CDN infrastructure spanning approximately 3,000–4,000 servers, about 10 locations, and more than 65 Gbps peak traffic | Strong | Lead summary and ISPrime experience |
| Low-level systems software | PrimeHTTPD in C on FreeBSD; FreeBSD kernel modules; TAFOS x86 kernel work | Strong | Lead technical highlights and projects |
| Distributed systems and infrastructure platforms | Multi-location CDN, deployment systems, authentication, monitoring, traffic analysis, and operational tooling | Strong | Summary, highlights, ISPrime bullets |
| Large-scale networking | HTTP/CDN serving, TCP/IP tuning, DNS monitoring, packet analysis, DDoS detection and mitigation | Strong | Skills, highlights, projects |
| Runtime and event-loop design | Single main PrimeHTTPD process, one primary kqueue, non-blocking sockets, accept filtering, configurable blocking-I/O workers | Strong | PrimeHTTPD bullets |
| Storage and I/O optimization | sendfile(), SF_NODISKIO, file-descriptor caching, asynchronous open/sendfile worker handoff, gzip memory cache | Strong | PrimeHTTPD bullets |
| Inter-process communication | sendmsg()-based job dispatch and descriptor passing between main process and I/O workers | Strong | PrimeHTTPD bullets |
| Scheduling / workload assignment | mmap()-shared worker state and least-busy-worker selection | Moderate to strong | PrimeHTTPD architecture bullet |
| Reliability and operational ownership | 24/7 production infrastructure, monitoring, failover-oriented operations, incident response, infrastructure modernization | Strong | Summary and experience |
| Observability and debugging | PrimeDump, PrimeDNSTop, telemetry, health alerting, GDB, packet-level diagnosis | Strong | Highlights and projects |
| Security and incident response | DDoS detection/mitigation, DNS recursion-attack detection, IPFW integration, authentication systems | Strong | Skills and ISPrime bullets |
| Platform tooling / leverage for others | Deployment automation, shared libraries, engineering standards, AI-assisted workflows, CI/CD and security scanning | Strong | Advantive experience |
| Kubernetes and container infrastructure | Implemented Docker, Kubernetes, Terraform, Azure DevOps, CI/CD, and security-scanning workflows; additional runtime experimentation documented separately | Moderate | Skills and Advantive bullet, carefully worded |
| Operating-system internals | FreeBSD syscalls, kernel modules, kqueue, sendfile, signals, mmap, descriptor passing; educational x86 kernel | Strong | Skills and selected projects |
| Hardware-aware optimization | Kernel-assisted zero-copy I/O, socket tuning, accept filters, minimizing copies/context switches | Strong for host/runtime; not GPU-specific | PrimeHTTPD and summary |
| Benchmarking and disciplined measurement | Production concurrency and traffic metrics; historical performance comparison requires further documentary support | Moderate | Use verified scale, avoid unsupported comparative claims |
| Cross-functional collaboration | Architecture Team work, standards, shared libraries, documentation, platform direction | Moderate to strong | Advantive bullet |
| Ambiguity and ownership | Architected and personally implemented core systems while also operating the business/infrastructure | Strong | Summary and leadership bullets |
| Agent infrastructure / AI tooling | AI-assisted engineering workflows, MCPs, local LLM and agent-tool experimentation | Emerging | Secondary skills only unless strengthened |
| GPU infrastructure | No verified direct production GPU fleet ownership | Gap | Do not claim |
| RDMA / NCCL / collective communication | No verified experience | Gap | Do not claim |
| Large-scale Kubernetes scheduler internals | Kubernetes workflow experience exists; deep scheduler/control-plane production ownership not yet verified | Gap / partial | Do not overstate |

## Highest-Value Evidence

### PrimeHTTPD

- Configurable number of I/O worker processes, with the latency-sensitive networking core remaining in one main process.
- One primary `kqueue`; only the main process called `accept()`.
- FreeBSD HTTP accept filtering so accept readiness occurred only when an HTTP connection/request was waiting.
- Blocking file opens and disk-backed sends were delegated to workers.
- `sendmsg()` transferred jobs and file/socket descriptors between processes.
- Main process used `sendfile()` with `SF_NODISKIO`; work that risked blocking was handed to an I/O worker with file descriptor, socket descriptor, offset, and byte count.
- Workers returned descriptors after completing work.
- Shared `mmap()` state exposed worker activity and enabled least-busy-worker assignment.
- Configurable socket-write threshold.
- File-descriptor cache and in-memory gzip cache.
- Chunked transfer encoding, ETags, conditional GET, PrimeAuth integration, wildcard rewrites, and PCRE2 regular-expression rewrites.
- `SIGUSR1` configuration reloads.
- Approximately 200 production deployments and more than 150,000 concurrent connections.

### CDN and Infrastructure Platform

- Approximately 3,000–4,000 servers across the broader infrastructure.
- Approximately 10 locations.
- More than 65 Gbps peak traffic.
- Custom HTTP serving, authentication, monitoring, deployment, security, packet analysis, DNS analysis, and DDoS tooling.

### Systems and Kernel Work

- FreeBSD kernel modules including VirtualDir, KeepClean, and StatCache.
- VirtualDir intercepted filesystem-related syscalls and remapped paths transparently from configuration.
- TAFOS educational x86 kernel included a custom MBR bootloader, protected mode, IDT, memory allocation, port I/O, VGA output, and GDB support.

## Claims Requiring Caution

- Do not claim PrimeHTTPD was the first event-driven web server or first C10K solution.
- Do not state exact Apache/nginx benchmark superiority without contemporaneous benchmark evidence.
- Treat 3,000–4,000 servers and approximately 10 locations as estimates.
- Do not claim direct GPU, RDMA, NCCL, or collective-communication experience.
- Do not characterize Kubernetes experience as deep production control-plane or scheduler engineering without additional evidence.

## Recommended Interview Emphasis

1. PrimeHTTPD event-loop and blocking-I/O separation.
2. Descriptor passing and ownership across processes.
3. Shared-memory worker scheduling and operational visibility.
4. Production networking scale and incident response.
5. Kernel modules and syscall-level path virtualization.
6. DDoS detection and tooling built from packet/DNS evidence.
7. Architecture-team work that creates leverage for other engineers.
