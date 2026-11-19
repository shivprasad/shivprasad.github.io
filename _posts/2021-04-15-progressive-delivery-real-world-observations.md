---
title: "Progressive Delivery: Real-World Observations"
date: 2021-04-15 02:00:00 -0700
categories:
  - Blog
  - General
tags:
  - feature-flags
  - progressive-delivery
authors:
  - shiv
---

We’ve been running more canaries and blue-green rollouts lately.

What’s working:
- Canary release + alerting = confidence boost
- Feature toggles let us decouple deployment and launch

Still rough:
- Managing toggle sprawl
- Data drift between versions

Tools: LaunchDarkly + Flagger + custom metrics dashboards.

Once you go progressive, hard to go back.
