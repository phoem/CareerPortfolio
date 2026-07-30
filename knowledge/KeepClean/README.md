---
type: Kernel Module
title: KeepClean
description: Production FreeBSD kernel module for execution monitoring, system-asset protection, and telemetry.
tags: [freebsd, kernel, security, telemetry, syscalls]
generated:
  at: 2026-07-12T00:00:00Z
status: partial
owner: Jordan Newman
evidence_status: confirmed
---

# KeepClean

## Summary

KeepClean is a production FreeBSD kernel module built to monitor execution activity, protect system assets, and report telemetry to user-space services.

## Confirmed Capabilities

- hooks system calls;
- monitors process or execution activity;
- protects selected system assets;
- reports telemetry to user-space services.

## Evidence Quality

- Kernel-module authorship, production use, syscall hooking, protection behavior, and user-space telemetry are confirmed qualitative evidence.
- No deployment-scale or performance metric is currently resume-safe.

## Open Questions

- exact system calls and event types;
- policy and configuration format;
- enforcement behavior;
- user-space protocol;
- deployment footprint and duration.
