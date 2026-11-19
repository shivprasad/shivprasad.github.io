---
title: "Docker Slimming Strategies That Worked"
date: 2019-05-28 06:00:00 -0700
categories:
  - Tech
  - Containers
tags:
  - containers
  - docker
authors:
  - shiv
---

We reviewed our Docker image sizes this quarter and realized most of our base images were bloated.

What helped:
- Multi-stage builds
- Using Alpine-based images
- Explicitly removing temp files and build artifacts
- Using `.dockerignore` properly

Bonus: [dive](https://github.com/wagoodman/dive) helped visualize image layers and waste.

Result: average image size went from 1.2GB → 300MB. Faster CI, faster deploys.
