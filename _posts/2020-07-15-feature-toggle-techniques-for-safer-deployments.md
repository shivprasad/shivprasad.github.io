---
title: "Feature Toggle Techniques for Safer Deployments"
date: 2020-07-15 04:45:00 -0700
categories:
  - Blog
  - General
tags:
  - deployment
  - feature-toggles
authors:
  - shiv
---

Feature toggles (or flags) aren’t just about hiding features. They’re critical to safe deploys and continuous delivery.

Key types:
- Release toggle
- Ops toggle
- Experiment toggle
- Permission toggle

Good practices:
- Add expiry dates
- Track toggle usage in metrics
- Avoid toggles in shared libraries

Tools used: LaunchDarkly, Unleash, config-driven toggles
