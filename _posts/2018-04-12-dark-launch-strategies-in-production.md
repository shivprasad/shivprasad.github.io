---
title: "Dark Launch Strategies in Production"
date: 2018-04-12 08:00:00 -0700
categories:
  - Blog
  - General
tags:
  - dark-launch
  - feature-flags
authors:
  - shiv
---

Not all launches should be visible. One of the most powerful tools in my backend toolbox is the dark launch — shipping code without exposing it to users.

In one project, we wanted to roll out a new scoring algorithm behind the scenes. Here’s the approach:
- Ship the logic to production behind a feature flag
- Run both old and new code paths in parallel
- Collect metrics and output differences
- Validate real-world impact before enabling it

Tools used: `Unleash`, custom logging hooks, and Grafana dashboards for monitoring divergence.

This method gave us confidence without panic. No failed deploy rollbacks, just quiet data gathering until we were sure.
