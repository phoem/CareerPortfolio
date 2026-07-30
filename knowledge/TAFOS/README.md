---
type: Operating System Project
title: TAFOS Operating System
description: Educational x86 operating-system kernel written in C and assembly.
tags: [c, assembly, x86, operating-systems, kernel, bootloader]
generated:
  at: 2026-07-12T00:00:00Z
status: partial
owner: Jordan Newman
evidence_status: confirmed
---

# TAFOS Operating System

## Summary

TAFOS is an educational x86 operating-system project written in C and assembly.

## Confirmed Implementation

- custom MBR bootloader;
- transition to protected mode;
- interrupt descriptor table;
- heap allocator;
- hardware port I/O;
- VGA text output;
- GDB debugging support.

## Evidence Quality

- The implementation items listed above are confirmed qualitative evidence.
- The project is educational; production-use, scale, reliability, and performance claims are not supported.

## Open Questions

- scheduler and process model;
- memory-management scope;
- filesystem or storage support;
- networking support;
- current build and emulator workflow.
