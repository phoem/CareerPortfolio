---
type: Kernel Module
title: StatCache
description: FreeBSD kernel instrumentation for stat and lstat filesystem activity.
tags: [freebsd, kernel, filesystem, performance, observability]
timestamp: 2026-07-12T00:00:00Z
status: partial
owner: Jordan Newman
evidence_status: confirmed
---

# StatCache

## Summary

StatCache is a FreeBSD kernel module built to instrument `stat()` and `lstat()` activity for filesystem visibility and performance analysis.

## Confirmed Capabilities

- kernel-level instrumentation of `stat()` and `lstat()`;
- filesystem activity visibility;
- performance-analysis support.

## Open Questions

- collection and aggregation architecture;
- user-space interface;
- production deployment footprint;
- measured findings and performance overhead.
