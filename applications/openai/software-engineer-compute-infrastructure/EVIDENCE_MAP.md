# Evidence Map - OpenAI Software Engineer, Compute Infrastructure

## Positioning

Jordan's strongest fit is low-level systems and runtime engineering, large-scale networking, reliability and observability, infrastructure tooling, and compute-foundation abstractions. His direct production evidence is CPU-, network-, and storage-I/O-oriented. The application must not imply production GPU-fleet, RDMA, NCCL, collective-communication, or Kubernetes control-plane ownership.

## Requirement-to-Evidence Map

| Requirement | Class | Resume evidence | Supporting OKF concept | Metric or scope | Strength | Gap or action |
|---|---|---|---|---|---|---|
| Build and optimize reliable systems software for large-scale compute infrastructure | Required | PrimeHTTPD and production CDN runtime | [PrimeHTTPD](../../../knowledge/PrimeHTTPD/README.md); [CDN Platform](../../../knowledge/CDN_Platform/README.md) | About 200 runtime servers; more than 150,000 concurrent connections; broader platform of approximately 3,000-4,000 servers | Direct | Keep language focused on host/runtime and networking systems, not GPU training infrastructure |
| Build, operate, or improve demanding production infrastructure | Required | Architected and operated the ISPRIME hosting/CDN platform | [CDN Platform](../../../knowledge/CDN_Platform/README.md) | Approximately 3,000-4,000 servers, about 10 locations, more than 65 Gbps peak traffic, 24/7 workloads | Direct | Preserve all estimate qualifiers |
| Distributed systems and infrastructure platforms | Required | Multi-location CDN plus monitoring, authentication, security, deployment, and operational systems | [CDN Platform](../../../knowledge/CDN_Platform/README.md) | Multi-location production platform | Direct | Avoid undocumented content-placement, replication, or routing details |
| Operating systems, kernel, or runtime behavior | Relevant area | C and FreeBSD runtime; production kernel modules; educational x86 kernel | [PrimeHTTPD](../../../knowledge/PrimeHTTPD/README.md); [VirtualDir](../../../knowledge/VirtualDir/README.md); [KeepClean](../../../knowledge/KeepClean/README.md); [StatCache](../../../knowledge/StatCache/README.md); [TAFOS](../../../knowledge/TAFOS/README.md) | PrimeHTTPD production deployment; VirtualDir on approximately 30 servers for approximately 5-8 years | Direct | Keep TAFOS explicitly educational |
| Large-scale networking systems and protocols | Relevant area | HTTP/CDN serving, TCP/IP tuning, DNS monitoring, packet analysis, and DDoS operations | [PrimeHTTPD](../../../knowledge/PrimeHTTPD/README.md); [PrimeDump](../../../knowledge/PrimeDump/README.md); [PrimeDNSTop](../../../knowledge/PrimeDNSTop/README.md) | More than 65 Gbps platform peak traffic | Direct | No undocumented packet-rate or mitigation-effectiveness metrics |
| Profile, benchmark, and optimize bottlenecks | Responsibility / signal | Kernel-aware I/O-path design, production concurrency evidence, GDB and packet-level diagnosis | [PrimeHTTPD](../../../knowledge/PrimeHTTPD/README.md); [StatCache](../../../knowledge/StatCache/README.md); [PrimeDump](../../../knowledge/PrimeDump/README.md) | More than 150,000 concurrent connections | Adjacent | Direct profiling/benchmark records are not yet documented; do not claim comparative benchmark leadership |
| Storage and I/O performance | Relevant area | `sendfile()`/`SF_NODISKIO`, descriptor caching, gzip caching, blocking-I/O worker handoff | [PrimeHTTPD](../../../knowledge/PrimeHTTPD/README.md) | Production HTTP/CDN serving runtime | Direct for local I/O path | No verified distributed-filesystem or object-storage ownership |
| Scheduling and workload assignment | Relevant area | Least-busy I/O-worker assignment from shared `mmap()` state | [PrimeHTTPD](../../../knowledge/PrimeHTTPD/README.md) | Configurable worker pool within each runtime | Adjacent | Do not equate process-level dispatch with cluster scheduling |
| Observability, fleet health, and difficult incident diagnosis | Relevant area / signal | Shared worker telemetry, packet and DNS analysis, monitoring, health alerting, cross-layer incident diagnosis | [PrimeHTTPD](../../../knowledge/PrimeHTTPD/README.md); [PrimeDump](../../../knowledge/PrimeDump/README.md); [PrimeDNSTop](../../../knowledge/PrimeDNSTop/README.md); [CDN Platform](../../../knowledge/CDN_Platform/README.md) | 24/7 customer-facing infrastructure | Direct | Hardware-health and accelerator-failure experience is not documented |
| Turn operational lessons into stronger systems and tooling | Required responsibility | Built monitoring, security, traffic-analysis, deployment, authentication, and DDoS systems from production needs | [CDN Platform](../../../knowledge/CDN_Platform/README.md) | Production platform over long-term ownership | Direct | No quantified incident-rate or recovery-time outcome documented |
| Kubernetes, CaaS, and container infrastructure | Relevant area | Professional Kubernetes delivery workflows; Docker and Terraform platform work | [Advantive Role](../../../knowledge/Advantive_Role/README.md); [Container Runtime and Kubernetes Experience](../../../knowledge/Container_Runtime_Experience/README.md) | Confirmed qualitative production workflow experience | Adjacent | kubelet, containerd, and runc work is experimental; no scheduler/control-plane ownership |
| Developer tools, workflows, APIs, and platform abstractions | Relevant area / signal | Architecture Team, shared platform engineering, developer tooling, shared libraries, documentation, CI/CD, and AI-assisted workflows | [Advantive Role](../../../knowledge/Advantive_Role/README.md) | Cross-team qualitative scope | Direct | Capture named tools and measurable developer impact if Jordan supplies them |
| Hardware-aware performance optimization | Relevant area | FreeBSD accept filters, zero-copy transfer, socket tuning, and disk-I/O isolation | [PrimeHTTPD](../../../knowledge/PrimeHTTPD/README.md) | Production runtime across approximately 200 servers | Direct for host/runtime | Not GPU-, firmware-, or topology-specific |
| Debug complex behavior across software, hardware, networking, and workloads | Required | Cross-layer performance, reliability, network, and abuse diagnosis; GDB and packet/DNS tooling | [CDN Platform](../../../knowledge/CDN_Platform/README.md); [PrimeDump](../../../knowledge/PrimeDump/README.md); [PrimeDNSTop](../../../knowledge/PrimeDNSTop/README.md) | 24/7 production operations | Direct across software/network layers; adjacent for hardware | Do not imply accelerator or firmware debugging |
| Clear communication, collaboration, ownership, and durable solutions | Required / contextual | Architecture Team collaboration plus long-term platform architecture, implementation, and operations | [Advantive Role](../../../knowledge/Advantive_Role/README.md); [CDN Platform](../../../knowledge/CDN_Platform/README.md) | Cross-team current role; long-term infrastructure ownership | Direct | Current-role outcomes remain qualitative |
| GPU infrastructure | Relevant area | None | - | - | Missing | Do not claim |
| RDMA, NCCL, or collective communication | Relevant area | None | - | - | Missing | Do not claim |
| Accelerator topology, firmware, and thermals | Contextual | None | - | - | Missing | Do not claim |
| Agent infrastructure with sandboxed execution | Team area | AI-assisted engineering workflows only | [Advantive Role](../../../knowledge/Advantive_Role/README.md) | Emerging workflow experience | Adjacent | Do not claim production sandboxed agent infrastructure |

## Highest-Value Resume Evidence

1. Production infrastructure scale: approximately 3,000-4,000 servers, about 10 locations, and more than 65 Gbps peak traffic.
2. PrimeHTTPD: a production C/FreeBSD runtime deployed across approximately 200 servers and supporting more than 150,000 concurrent connections.
3. Event and I/O architecture: one primary `kqueue`, blocking-I/O workers, `sendmsg()` descriptor passing, shared `mmap()` worker telemetry and dispatch, and `sendfile()` with `SF_NODISKIO`.
4. Network operations and observability: PrimeDump, PrimeDNSTop, DDoS systems, monitoring, telemetry, and incident diagnosis.
5. Kernel and systems work: VirtualDir, KeepClean, StatCache, and TAFOS, with production and educational boundaries preserved.
6. Current platform leverage: architecture decisions, shared engineering workflows, Kubernetes, Docker, Terraform, Azure DevOps, CI/CD, security scanning, developer tooling, and AI-assisted workflows.

## Open Evidence Questions

- What named shared libraries, platform components, or developer tools did Jordan personally deliver at Advantive?
- What measurable developer-productivity, delivery, reliability, or security outcomes resulted from the current-role work?
- What production Kubernetes operations or troubleshooting did Jordan personally perform?
- Are profiler traces, benchmark records, or contemporaneous PrimeHTTPD performance evidence available?
- What documented CDN routing, failover, content-placement, deployment, or rollback mechanisms can be added safely?
