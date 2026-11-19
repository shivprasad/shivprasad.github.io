---
title: "Google Cloud Run: A Developer’s Review"
date: 2020-05-03 04:00:00 -0700
categories:
  - Blog
  - General
tags:
  - cloud-run
  - gcp
  - serverless
authors:
  - shiv
---

[Cloud Run](https://cloud.google.com/run) abstracts away Kubernetes but gives you container-based deploys. A great middle ground between serverless and container orchestration.

Pros:
- Auto-scaling to zero
- Built-in HTTPS
- Deploy with Dockerfile

Limitations:
- 15-minute request timeout (back then)
- Cold starts still noticeable for larger images

We migrated two small services — and cost dropped while DX improved.
