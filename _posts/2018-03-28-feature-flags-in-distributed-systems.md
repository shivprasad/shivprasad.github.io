---
title: "Feature Flags in Distributed Systems"
date: 2018-03-28 11:00:00 -0700
categories:
  - Tech
  - Microservices
tags:
  - feature-flags
  - microservices
authors:
  - shiv
---

Rolling out a feature safely across dozens of services? You’ll need more than a `if (enabled)` check.

We used LaunchDarkly and later togglz to gate feature access based on:
- Service version
- Region or data center
- Random sampling

Tip: avoid coupling flags with code logic too tightly. Flags are transient — your code isn’t.

And always have a kill switch path. Fail open or closed — never undefined.
