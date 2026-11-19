---
title: "Infra Config as Code: Lessons from the Field"
date: 2021-06-22 09:00:00 -0700
categories:
  - Blog
  - General
tags:
  - iac
  - infrastructure
authors:
  - shiv
---

We finally consolidated Terraform + Helm + GitHub Actions into a unified IaC setup.

Highlights:
- Declarative everything
- PR-based review workflows
- Staging/production promotion pipelines

It took time — but totally worth it for reproducibility and audit trails.

If you're still copy-pasting configs, start small and iterate.
