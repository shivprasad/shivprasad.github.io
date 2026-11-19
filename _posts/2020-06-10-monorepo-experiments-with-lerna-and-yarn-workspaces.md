---
title: "Monorepo Experiments with Lerna and Yarn Workspaces"
date: 2020-06-10 05:00:00 -0700
categories:
  - Blog
  - General
tags:
  - lerna
  - monorepo
  - yarn
authors:
  - shiv
---

We started merging multiple micro frontends and shared libs into a monorepo.

Tools: [Lerna](https://lerna.js.org/), [Yarn Workspaces](https://classic.yarnpkg.com/en/docs/workspaces/)

Benefits:
- Easier dependency updates
- Unified CI/CD pipelines
- Better visibility into breakages

Issues:
- Build performance can degrade
- Requires discipline around boundaries

Verdict: Promising for now — needs tooling maturity.
