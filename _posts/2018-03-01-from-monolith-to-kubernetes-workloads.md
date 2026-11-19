---
title: "From Monolith to Kubernetes Workloads"
date: 2018-03-01 04:00:00 -0800
categories:
  - Tech
  - Kubernetes
tags:
  - kubernetes
  - migration
authors:
  - shiv
---

We finally made the leap: moved a legacy Java monolith to Kubernetes.

Here’s what helped:
- Broke out background jobs as independent CronJobs
- Converted WAR to fat JARs using Spring Boot
- Used ConfigMaps + Secrets to manage environment parity

Our CI pipeline triggered builds and published images to a private registry. Helm took care of deployment templates.

One pain point? Stateful storage. We had to rethink our use of local file writes and convert some features to S3-based persistence.

But overall, the transition was smoother than expected — with improved rollout control and monitoring.
