---
title: "Using Skaffold for Kubernetes Development"
date: 2018-11-01 09:00:00 -0700
categories:
  - Tech
  - Kubernetes
tags:
  - dev-workflow
  - skaffold
authors:
  - shiv
---

Local dev for Kubernetes can be painful. Skaffold helped bridge that by automating the loop: build → push → deploy → verify.

We defined a `skaffold.yaml` for our Spring Boot app and used:
- `buildpacks` for container builds
- `kubectl` for apply/delete
- `skaffold dev` to watch changes

Outcome? Reduced our feedback cycle to seconds.

Still maturing, but already a time-saver for iterative development inside k8s clusters.
