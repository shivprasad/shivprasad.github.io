---
title: "Slimming Down Docker Images"
date: 2023-03-12 04:00:00 -0700
categories:
  - Tech
  - Containers
tags:
  - containers
  - docker
authors:
  - shiv
---

Tips from recent container optimization:

- Use Alpine base images
- Multi-stage builds for pruning
- Avoid adding unnecessary tools (curl, git, etc.)

Got an image down from 1.2 GB → 180 MB. Worth the effort!
