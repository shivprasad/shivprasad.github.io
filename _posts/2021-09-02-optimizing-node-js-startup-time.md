---
title: "Optimizing Node.js Startup Time"
date: 2021-09-02 04:00:00 -0700
categories:
  - Blog
  - General
tags:
  - nodejs
  - performance
authors:
  - shiv
---

We had a startup time issue on our microservices — especially noticeable in local dev.

What helped:
- Deferred `require()` calls
- Breaking up init logic
- Profiling with `--trace-startup`

Bonus: Using esbuild for bundling shaved off more seconds.

Small tweaks, big dev experience win.
