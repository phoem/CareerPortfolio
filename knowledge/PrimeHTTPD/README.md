---
type: Software Project
title: PrimeHTTPD
description: High-performance non-blocking event-driven HTTP and CDN server written in C for FreeBSD.
tags: [c, freebsd, http, cdn, networking, performance, kqueue]
timestamp: 2026-07-12T00:00:00Z
status: partial
owner: Jordan Newman
evidence_status: confirmed
deployment: Approximately 200 production servers; more than 150,000 concurrent connections.
---

# PrimeHTTPD

## Summary

PrimeHTTPD is a high-performance, non-blocking, event-driven HTTP server written in C for FreeBSD. It was designed from scratch around `kqueue` and FreeBSD kernel capabilities, then used as a core component of a production content delivery network.

## Personal Ownership

Jordan Newman architected and implemented PrimeHTTPD and the surrounding CDN software platform.

## Architecture and Implementation

- non-blocking, event-driven networking;
- `kqueue`-based event processing;
- persistent HTTP connections;
- `sendfile()`-based zero-copy file transfer;
- `SF_NODISKIO` to avoid blocking the event loop on disk reads;
- dedicated I/O workers for disk operations that would otherwise block;
- `O_NONBLOCK` sockets;
- `TCP_NODELAY` and `TCP_NOPUSH` socket behavior and tuning;
- FreeBSD `accept_filter_http` support;
- design intended to minimize copies, blocking operations, and unnecessary context switching.

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

## Resume-Ready Descriptions

### Detailed systems version

Architected and implemented PrimeHTTPD, a high-performance, non-blocking, `kqueue`-based HTTP/CDN server in C for FreeBSD. Designed an event-driven architecture supporting persistent HTTP connections, `sendfile()` zero-copy transfers, `SF_NODISKIO`, `TCP_NODELAY`, `TCP_NOPUSH`, `O_NONBLOCK`, and `accept_filter_http`; implemented dedicated I/O workers to offload disk operations that would otherwise block the networking event loop.

Optimized the server around FreeBSD kernel capabilities, minimizing copies, context switching, and blocking operations while scaling across large production deployments.

### Recruiter-facing version

Designed and built the high-performance C web server and supporting software platform that powered a multi-location production CDN serving high-traffic customer workloads.

### Architect version

Architected the HTTP serving and CDN software platform for infrastructure spanning thousands of servers and multiple points of presence, combining a custom FreeBSD event-driven server, kernel-aware performance optimizations, operational tooling, and custom systems software.

## Open Questions

- exact CDN features implemented directly inside PrimeHTTPD;
- cache-control, byte-range, validation, logging, configuration reload, and routing details;
- worker/process topology and multi-core scaling design;
- benchmark methodology and comparative performance results;
- deployment automation and content-distribution workflow;
- exact request-time relationship between PrimeHTTPD, VirtualDir, and other CDN components.
