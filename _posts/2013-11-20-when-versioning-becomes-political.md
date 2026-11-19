---
title: "When Versioning Becomes Political"
date: 2013-11-20 05:20:00 -0800
categories:
  - Blog
  - General
tags:
  - api
  - design-process
  - governance
  - versioning
authors:
  - shiv
---

We introduced a new API versioning policy last week. What should’ve been a 15-minute dev conversation turned into a multi-team negotiation.

Why? Because **versioning isn’t just technical—it’s political**.

APIs are consumed by humans. Teams invest in assumptions. So changing an endpoint means changing processes, docs, dashboards, expectations.

What worked:
- Clear deprecation timelines
- Changelogs written in plain English
- API linter checks in CI

Lesson: If your API breaks people’s trust, they stop adopting your APIs.
