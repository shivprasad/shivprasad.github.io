---
title: "How Build Times Reveal Organizational Health"
date: 2013-10-31 09:40:00 -0700
categories:
  - Blog
  - General
tags:
  - ci
  - build-systems
  - dev-productivity
  - tooling
authors:
  - shiv
---

Around October 2013, I became obsessed with measuring build times—and not just for performance.

Slow builds often revealed deeper issues:
- Poor modularization
- Over-engineered dependency graphs
- Flaky tests masking underlying debt

I started using [Gradle Build Scans](https://scans.gradle.com/) and simple shell timers to identify bottlenecks. Cutting our build time from 18 min to 6 min had a huge morale and velocity impact.

**Fast builds = fast feedback = faster teams.** It's more than speed; it's about momentum.
