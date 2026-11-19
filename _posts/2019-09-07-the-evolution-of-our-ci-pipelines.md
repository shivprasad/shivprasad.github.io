---
title: "The Evolution of Our CI Pipelines"
date: 2019-09-07 01:30:00 -0700
categories:
  - Blog
  - General
tags:
  - ci
  - cd
authors:
  - shiv
---

Over the last year, we evolved our CI/CD pipelines from basic test runners to full deployment orchestrators.

Changes made:
- Added static checks: lint, style, dep vulnerability scans
- Parallel test execution via matrix builds
- Pre-prod environments spun on every PR

Tools:
- GitLab CI + custom runners
- Helm + ArgoCD for Kubernetes deployments

Faster feedback loops = happier teams.
