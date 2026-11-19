---
title: "Moving from CircleCI to GitHub Actions"
date: 2022-11-20 05:30:00 -0800
categories:
  - Blog
  - General
tags:
  - ci/cd
  - github-actions
authors:
  - shiv
---

We switched a small project from CircleCI to GHA.

- Native integration with GitHub = fewer tokens
- Easier caching, though limits still sting
- YAML everywhere 😅

Net gain for simple pipelines. Circle still better for matrix-heavy builds.
