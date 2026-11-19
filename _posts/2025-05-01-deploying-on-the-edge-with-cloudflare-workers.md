---
title: "Deploying on the Edge with Cloudflare Workers"
date: 2025-05-01 01:30:00 -0700
categories:
  - Blog
  - General
tags:
  - cloudflare
  - edge
authors:
  - shiv
---

Moved a few latency-sensitive endpoints to Cloudflare Workers.

- Fast cold start times
- Integration with KV and D1 is handy
- Still has per-request CPU limits

Edge is ideal for personalization and auth-lite endpoints.
