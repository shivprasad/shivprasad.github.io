---
title: "Speeding up GitHub Actions with Smart Caching"
date: 2022-09-15 06:45:00 -0700
categories:
  - Blog
  - General
tags:
  - ci/cd
  - github-actions
authors:
  - shiv
---

Found a few wins for caching in GitHub Actions:

- Cache npm/yarn/pnpm folders per branch
- Use `restore-keys` for fallback matching
- Avoid cache bloat by pruning often

Small tweaks cut build times from 3m → 45s. Worth the setup!
