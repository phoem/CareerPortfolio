---
type: Kernel Module
title: KeepClean
description: FreeBSD kernel module for monitoring execution activity, protecting system assets, and reporting telemetry.
tags: [freebsd, kernel, security, telemetry, syscalls]
timestamp: 2026-07-11T00:00:00Z
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

## Open Questions

- exact system calls and event types;
- policy and configuration format;
- enforcement behavior;
- user-space protocol;
- deployment footprint and duration.
