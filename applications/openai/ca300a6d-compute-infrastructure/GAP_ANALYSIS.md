# Gap Analysis — OpenAI Software Engineer, Compute Infrastructure

## Strong Direct Match

- Large-scale production infrastructure ownership: approximately 3,000-4,000 servers across 10 locations and more than 65 Gbps of peak traffic.
- Low-level systems and runtime engineering in C and FreeBSD, including kernel modules and a high-concurrency production HTTP/CDN runtime.
- High-performance networking, storage-I/O path design, observability, packet and DNS analysis, BGP/NetFlow systems work, DDoS mitigation, and cross-layer diagnosis.
- Long-term operational ownership under 24/7 reliability demands, including purpose-built monitoring and health-check systems.
- Developer-platform leverage through reusable pipelines, templates, deployment gates, self-hosted runners, APIs, CLI tools, and shared engineering practices.
- Direct implementation of local agent infrastructure with sandboxing, permissions, workflows, approvals, model routing, MCP integrations, and auditability.
- Comfort with ambiguity and end-to-end technical ownership, including leadership of major projects and up to 10 employees.

## Adjacent Evidence

- Kubernetes experience is direct for professional delivery workflows but not for production scheduler, control-plane, kubelet, containerd, or runc development.
- PrimeHTTPD worker assignment demonstrates scheduling and telemetry principles at runtime/process scope, not cluster-scheduler ownership.
- Hardware-aware optimization is strong at the CPU, operating-system, NIC/socket, and storage-I/O boundary, not for accelerators, firmware, thermals, or topology.
- CPU profiling with GDB, Valgrind, and Linux `perf` is confirmed, but formal benchmark records and measured improvements are not documented.
- Nexus directly demonstrates agent-infrastructure design and implementation, but its production scale and external adoption are unknown.

## Genuine Gaps

- No documented production GPU-cluster or accelerator-infrastructure ownership.
- No documented RDMA, NCCL, or collective-communication work.
- No documented GPU profiling, firmware upgrade automation, thermal analysis, or accelerator-topology optimization.
- No verified distributed-filesystem or large-scale storage-platform ownership.
- No production Kubernetes control-plane or scheduler implementation.

## Tailoring Decision

Use the Backend / Infrastructure Engineer resume as the base. Lead with proven scale, durable systems software, network and storage-I/O optimization, fleet observability, developer-platform leverage, and Nexus agent infrastructure. Do not dilute the strongest evidence by suggesting unverified accelerator experience. The posting is explicitly broad and does not require every candidate to cover every infrastructure layer.
