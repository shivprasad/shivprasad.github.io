---
title: "Radar Reaction: Feature Switches as Default Strategy"
date: 2015-02-12 01:15:00 -0800
categories:
  - Tech
  - Frontend
tags:
  - feature-flags
  - release-strategy
  - thoughtworks-radar
authors:
  - shiv
---

[ThoughtWorks Radar Q1 2015](https://www.thoughtworks.com/radar/techniques/feature-switches) featured **Feature Switches** again — and rightfully so.

We've made toggles a *default design choice*. Every new feature ships behind one, no exceptions. This has helped us:
- Do trunk-based development confidently
- Rollout and rollback without redeploys
- Collect A/B data from real users

This year we even added **configurable toggles via ZooKeeper** with auto-refresh in Spring apps.

Feature switches aren't just about safety. They're about speed.
