---
type: Operating System Project
title: TAFOS Operating System
description: Educational x86 operating-system kernel written in C and assembly.
tags: [operating-systems, x86, c, assembly, bootloader, kernel]
timestamp: 2026-07-11T00:00:00Z
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

## Open Questions

- scheduler and process model;
- memory-management scope;
- filesystem or storage support;
- networking support;
- current build and emulator workflow.
