---
title: "Scaling Feature Flags Across Microservices"
date: 2020-04-07 03:30:00 -0700
categories:
  - Tech
  - Microservices
tags:
  - feature-flags
  - microservices
  - unleash
authors:
  - shiv
---

We've moved beyond static feature flags and started scaling them across teams.

Lessons learned:
- Central config isn’t enough. Team-level overrides are essential.
- Observability matters: Feature flag metrics should be first-class.
- Rollbacks need to be instant, not commit-based.

We evaluated [Unleash](https://www.getunleash.io/), LaunchDarkly, and homemade Redis setups.

Best practice? Start with a core abstraction that decouples feature evaluation from implementation.
