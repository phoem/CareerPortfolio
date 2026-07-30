---
type: Software Project
title: PrimeHTTPD
description: High-performance non-blocking event-driven HTTP and CDN server written in C for FreeBSD.
tags: [c, freebsd, http, cdn, networking, performance, kqueue, c10k]
timestamp: 2026-07-30T00:00:00Z
status: partial
owner: Jordan Newman
evidence_status: confirmed
deployment: Approximately 200 production servers; more than 150,000 concurrent connections.
---

# PrimeHTTPD

## Summary

PrimeHTTPD is a high-performance, non-blocking, event-driven HTTP server written in C for FreeBSD. Jordan intentionally designed it around the C10K concurrency problem and selected an event-driven `kqueue` architecture because he considered it the most efficient way to serve very large numbers of simultaneous connections without relying on a thread or process per connection. It was designed before publicly available event-driven web servers that solved C10K were available to him, then became a core component of a production content delivery network.

## Problem Solved

At the time PrimeHTTPD was conceived, Apache 1.3's process-oriented architecture imposed concurrency and efficiency limitations, Apache 2 was not yet a stable production alternative for Jordan's needs, and nginx had not yet been released. PrimeHTTPD was created to address the C10K problem directly through asynchronous event notification, non-blocking sockets, kernel-assisted file transfer, and careful avoidance of blocking operations in the networking path.

This historical context supports describing PrimeHTTPD as intentionally designed to solve C10K. It does not support claiming that it was the first web server to do so or that no unpublished or inaccessible implementation existed elsewhere.

## Personal Ownership

Jordan Newman architected and implemented PrimeHTTPD and the surrounding CDN software platform.

## Architecture and Implementation

- non-blocking, event-driven networking selected specifically to address C10K-scale concurrency;
- `kqueue`-based event processing;
- persistent HTTP connections;
- `sendfile()`-based zero-copy file transfer;
- `SF_NODISKIO` to avoid blocking the event loop on disk reads;
- dedicated I/O workers for disk operations that would otherwise block;
- `O_NONBLOCK` sockets;
- `TCP_NODELAY` and `TCP_NOPUSH` socket behavior and tuning;
- FreeBSD `accept_filter_http` support;
- design intended to minimize copies, blocking operations, unnecessary context switching, and per-connection overhead.

## CDN Platform Context

PrimeHTTPD was not only a standalone web server. It served as the foundation of a production CDN and included CDN-oriented capabilities. Jordan also built the CDN infrastructure and supporting software around it.

Known production context:

- approximately 3,000-4,000 servers across the broader infrastructure;
- approximately 10 CDN locations;
- peak traffic exceeding 65 Gbps;
- PrimeHTTPD deployed across approximately 200 production servers;
- support for more than 150,000 concurrent connections;
- high-traffic customer production workloads.

The platform also used [VirtualDir](/VirtualDir/README.md), [PrimeDump](/PrimeDump/README.md), [PrimeDNSTop](/PrimeDNSTop/README.md), and other custom operational software.

## Evidence

- **Exact qualitative fact:** PrimeHTTPD was intentionally architected to solve the C10K problem.
- **Exact qualitative fact:** Jordan selected an event-driven `kqueue` design because he judged it the most efficient concurrency model for that problem.
- **Historical-context claim:** At the time of development, Jordan was not aware of a publicly released web server that already solved C10K using the architecture he needed. Resume wording must preserve this narrower scope and must not claim universal or industry-wide priority.
- **Estimated production scale:** approximately 3,000-4,000 servers across the broader infrastructure and approximately 10 CDN locations.
- **Confirmed production scale:** PrimeHTTPD deployed across approximately 200 production servers, supported more than 150,000 concurrent connections, and participated in infrastructure carrying peak traffic exceeding 65 Gbps.

## Resume-Ready Descriptions

### Detailed systems version

Architected and implemented PrimeHTTPD, a high-performance HTTP/CDN server in C for FreeBSD intentionally designed around the C10K concurrency problem. Selected a non-blocking, event-driven `kqueue` architecture and used persistent connections, `sendfile()` zero-copy transfers, `SF_NODISKIO`, `TCP_NODELAY`, `TCP_NOPUSH`, `O_NONBLOCK`, and `accept_filter_http`; implemented dedicated I/O workers to keep blocking disk operations out of the networking event loop.

Optimized the server around FreeBSD kernel capabilities to minimize copies, context switching, and per-connection overhead, supporting more than 150,000 concurrent connections across approximately 200 production servers.

### Recruiter-facing version

Designed and built a high-performance C web server specifically to overcome C10K-era concurrency limits, then used it as the serving foundation for a multi-location production CDN handling high-traffic customer workloads.

### Architect version

Architected the HTTP serving and CDN software platform for infrastructure spanning thousands of servers and multiple points of presence, selecting an event-driven FreeBSD design to solve high-concurrency scaling constraints and combining kernel-aware performance optimizations, operational tooling, and custom systems software.

## Open Questions

- exact development and first-production dates for PrimeHTTPD;
- contemporaneous benchmark records or documentation that can support careful historical comparison with Apache and later nginx releases;
- exact CDN features implemented directly inside PrimeHTTPD;
- cache-control, byte-range, validation, logging, configuration reload, and routing details;
- worker/process topology and multi-core scaling design;
- benchmark methodology and comparative performance results;
- deployment automation and content-distribution workflow;
- exact request-time relationship between PrimeHTTPD, VirtualDir, and other CDN components.
