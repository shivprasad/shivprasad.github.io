---
title: "The Power of a Friday Feature Flag"
date: 2014-12-19 01:00:00 -0800
categories:
  - Blog
  - General
tags:
  - deployment
  - devops
  - feature-toggles
  - release-management
authors:
  - shiv
---

We used to fear Friday deploys. Now we deploy anytime, because we release via **feature flags**.

Toggles gave us:
- Safe rollouts
- Canary + A/B experiments
- Reversible changes without reverts

![Feature Flag Lifecycle](https://launchdarkly.com/blog/assets/images/feature-flags-diagram.png)

Feature Flag Lifecycle

Feature flags decoupled deploys from releases — and made our engineers confident, even on Fridays.
