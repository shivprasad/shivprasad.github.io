---
title: "Debugging Network Flakiness in Kubernetes Clusters"
date: 2017-11-03 06:00:00 -0700
categories:
  - Tech
  - Kubernetes
tags:
  - debugging
  - flaky-tests
  - networking
authors:
  - shiv
---

Our apps ran fine — until they didn’t. Sporadic 504s and TCP timeouts began surfacing intermittently.

### Root Causes Identified:

- Misconfigured readiness probes
- Aggressive connection reuse without keepalive
- DNS resolution delays under high pod churn

Tools like `tcpdump`, `dig`, and `kubectl describe` became my best friends. Eventually moved to Calico for more stable networking.

Lesson: Networking issues in Kubernetes often look like app bugs at first glance.
