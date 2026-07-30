# Gap Analysis — OpenAI Software Engineer, Compute Infrastructure

## Executive Assessment

This is a credible application when positioned around systems software, runtime behavior, large-scale networking, observability, reliability, and infrastructure tooling. The posting is intentionally broad and explicitly states that candidates are not expected to have experience at every layer. Jordan's profile should therefore emphasize depth in proven areas rather than attempting to appear GPU-specialized.

## Strong Matches

### Systems software

Jordan has unusually deep, directly relevant experience in C, FreeBSD, kernel interfaces, event-driven network servers, system calls, inter-process communication, shared memory, signals, descriptor passing, and kernel-assisted I/O.

### Production scale and ownership

The infrastructure scale—approximately 3,000–4,000 servers, roughly 10 locations, and more than 65 Gbps peak traffic—supports the posting's emphasis on demanding production environments, operational pressure, ownership, and durable improvements.

### Networking and data plane

PrimeHTTPD, the CDN platform, packet analysis, DNS analysis, TCP tuning, and DDoS mitigation strongly align with Core Network Engineering and data-plane work.

### Reliability and observability

Custom monitoring, traffic-analysis tools, health alerting, incident diagnosis, and operational software align with fleet health, observability, debugging, and reliability requirements.

### Infrastructure leverage

Architecture-team work, shared libraries, standards, CI/CD, security scanning, deployment automation, and AI-assisted workflows show the ability to make other engineers more effective.

## Partial Matches

### Kubernetes and orchestration

Jordan has real Kubernetes, Docker, Terraform, CI/CD, and deployment-workflow experience. Current evidence does not establish deep production ownership of Kubernetes scheduler internals, kubelet internals, or very large cluster control planes.

**Application treatment:** Include Kubernetes and container infrastructure in skills and current-role bullets, but avoid presenting it as the primary differentiator.

### Scheduling

PrimeHTTPD's least-busy-worker scheduling using shared worker state is technically relevant but much smaller in scope than cluster scheduling.

**Application treatment:** Use it as evidence of scheduling judgment and runtime design, not as a substitute for large-scale cluster-scheduler experience.

### Storage

PrimeHTTPD demonstrates sophisticated local file-I/O and caching design, but there is not yet strong evidence of distributed object stores, distributed filesystems, or cross-region storage platforms.

**Application treatment:** Emphasize I/O-path optimization, caching, descriptor management, and avoiding event-loop stalls.

### Agent infrastructure

Jordan uses AI-assisted development, MCPs, local LLM experimentation, and agent-oriented workflows, but evidence of production sandboxed agent execution infrastructure is not yet established.

**Application treatment:** Keep this as a modern supporting capability, not a headline claim.

## Material Gaps

### GPU fleet engineering

No verified direct experience operating large GPU fleets, tuning GPU kernels, diagnosing accelerator failures, or managing GPU capacity.

### RDMA, NCCL, and collective communication

No verified direct experience.

### Firmware, thermals, and accelerator topology

No verified production experience.

### Large-scale Kubernetes internals

No verified ownership of scheduler/control-plane internals at OpenAI-like scale.

## Risk Mitigation

- Lead with proven low-level systems and networking depth.
- State Kubernetes and cloud experience accurately and without inflated scope.
- Avoid keyword stuffing for GPU, RDMA, NCCL, or HPC technologies not supported by evidence.
- Use the posting's broad-team language to explain that Jordan is best matched to Compute Foundations, Core Network Engineering, observability/reliability, or infrastructure tooling.
- Highlight the ability to learn across layers, supported by kernel, networking, application, cloud, and architecture experience.

## Information That Would Improve the Application

1. PrimeHTTPD source code and representative configuration files.
2. More detail on CDN content distribution, routing, health checks, failover, and deployment.
3. More detail on automated DDoS detection, rule generation, and mitigation workflow.
4. Specific architecture-team decisions, libraries, standards, and measurable impact at Advantive.
5. Exact Kubernetes responsibilities and any work involving kubelet, containerd, CRI, namespaces, cgroups, networking, storage, or cluster troubleshooting.
6. Benchmark records, profiler output, or contemporaneous performance evidence for PrimeHTTPD.

## Recommendation

Proceed with the application. The resume should target **Systems Software / Compute Infrastructure / Networking / Reliability** rather than trying to mimic a GPU-infrastructure specialist. The strongest differentiator is the combination of hands-on low-level implementation and ownership of substantial 24/7 production infrastructure.
