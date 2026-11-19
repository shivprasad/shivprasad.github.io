---
title: "Designing Error Systems in Large Applications"
date: 2024-08-27 10:00:00 -0700
categories:
  - Blog
  - General
tags:
  - error-handling
  - systems-design
authors:
  - shiv
---

Revisited how we do error propagation.

- Use structured error types
- Don’t leak internals across layers
- Capture context without polluting call stacks

Getting this right saves hours in debugging.
