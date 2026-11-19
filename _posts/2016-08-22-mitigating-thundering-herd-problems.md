---
title: "Mitigating Thundering Herd Problems"
date: 2016-08-22 03:15:00 -0700
categories:
  - Blog
  - General
tags:
  - caching
  - thundering-herd
authors:
  - shiv
---

The thundering herd problem can overwhelm backends during cache expiration.

Techniques:
- Use request coalescing (single-flight)
- Stagger cache TTLs
- Introduce jitter into TTLs

Never let many clients hammer the backend for the same data at once.
