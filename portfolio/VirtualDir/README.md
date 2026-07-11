---
type: Kernel Module
title: VirtualDir
description: FreeBSD kernel module that transparently virtualizes filesystem paths through syscall interception and configurable remapping.
tags: [freebsd, kernel, filesystem, syscalls, virtualization, cdn]
timestamp: 2026-07-11T00:00:00Z
status: partial
owner: Jordan Newman
evidence_status: confirmed
deployment: Customer-facing across approximately 30 servers for approximately 5-8 years.
---

# VirtualDir

## Summary

VirtualDir is a FreeBSD loadable kernel module that virtualizes filesystem paths by intercepting filesystem-related system calls and transparently remapping matching paths according to a configuration file.

It allows multiple virtual-hosting environments to share a single physical filesystem layout without requiring chroot jails.

## Personal Ownership

Jordan Newman designed and developed the kernel module and its companion command-line management utility, `vdcli`.

## Architecture and Implementation

Documented implementation details include:

- FreeBSD loadable kernel module (`virtualdir.ko`);
- interception of filesystem-related system calls such as `open`, `stat`, `lstat`, and `readdir`;
- configurable prefix-based pathname remapping;
- transparent behavior for applications using the affected filesystem calls;
- a registered `virtualdir_control` syscall for configuration management;
- a user-space CLI, `vdcli`, which uses `modfind(3)` to locate the control syscall;
- runtime operations to load or reload configuration, dump the active configuration, and unload configuration;
- configuration stored in `/etc/virtualdir.conf`;
- FreeBSD kernel build environment using `bsd.kmod.mk`;
- dependency on `libisprime`, including `liblicense` and `libsafestring` for `vdcli`.

## Operational Context

VirtualDir was built to support production virtual-hosting and [CDN infrastructure](/CDN_Platform/README.md). It provided a kernel-level pathname abstraction so multiple hosting environments could share a physical filesystem organization while presenting different logical paths.

Known deployment information:

- customer-facing production use;
- deployed across approximately 30 servers;
- used for approximately 5-8 years.

## Management Commands

```text
vdcli 0    # load or reload /etc/virtualdir.conf
vdcli 1    # dump current configuration
vdcli 2    # unload configuration
```

## Resume-Ready Descriptions

### Detailed systems version

Designed and developed VirtualDir, a FreeBSD kernel module that virtualizes filesystem paths by intercepting filesystem-related system calls and transparently remapping paths according to configurable rules. Implemented kernel hooks for operations including `open`, `stat`, `lstat`, and directory enumeration, plus a custom control syscall and `vdcli` management utility for runtime configuration.

### Outcome-focused version

Built a production FreeBSD kernel pathname-virtualization layer that enabled multiple virtual-hosting environments to share a common physical filesystem layout without chroot jails, simplifying hosting and CDN content organization.

### Architect version

Designed a transparent kernel-level filesystem abstraction for multi-tenant hosting, separating logical content paths from physical storage layout while requiring no application-level changes.

## Relationship to the CDN Platform

VirtualDir complemented [PrimeHTTPD](/PrimeHTTPD/README.md) and the broader CDN platform by providing transparent path translation and flexible content organization for virtual-hosting environments.

## Open Questions

The following details have not yet been documented and should only be added after confirmation:

- exact syscall-hooking mechanism used for each supported FreeBSD version;
- configuration-file syntax and matching semantics;
- concurrency and locking design;
- performance overhead or benchmark results;
- failure handling and configuration validation;
- whether configuration reloads were atomic;
- exact PrimeHTTPD integration and request-path examples;
- deployment and rollback procedures.
