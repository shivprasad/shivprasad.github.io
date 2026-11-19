---
title: "esbuild vs SWC: Which One Should You Use?"
date: 2022-05-25 06:00:00 -0700
categories:
  - Tech
  - Frontend
tags:
  - esbuild
  - javascript
  - swc
authors:
  - shiv
---

Both `esbuild` and `swc` are amazing JS bundlers/transpilers.

Key takeaways:
- `esbuild` is written in Go — fastest build times
- `swc` is Rust-based — more Babel-compatible
- SWC powering Next.js is a big deal

For greenfield projects, either is great. Lean toward `swc` if you rely heavily on Babel transforms.
