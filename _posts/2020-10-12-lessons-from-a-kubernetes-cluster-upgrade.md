---
title: "Lessons from a Kubernetes Cluster Upgrade"
date: 2020-10-12 04:00:00 -0700
categories:
  - Tech
  - Kubernetes
tags:
  - cluster-upgrade
  - k8s
authors:
  - shiv
---

Upgraded our staging clusters to v1.19 this quarter.

Lessons learned:
- Always check deprecations beforehand (`kubectl deprecations`)
- Test ingress controller compatibility early
- Pod disruption budgets saved us from some flakiness

Tooling we used:
- `kustomize` for manifests
- `velero` for backups

Planning is everything. Production upgrade next quarter!
