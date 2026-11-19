---
title: "Kubernetes Security: A Checklist for Small Teams"
date: 2022-05-15 04:00:00 -0700
categories:
  - Tech
  - Kubernetes
tags:
  - kubernetes
  - security
authors:
  - shiv
---

Running k8s in production? Here’s a checklist we used:

- Use namespaces to segment workloads
- Enable RBAC and audit logging
- Limit container privileges
- Scan images for vulnerabilities
- Use NetworkPolicies to restrict traffic

Security by default takes work — but pays off in resilience.
