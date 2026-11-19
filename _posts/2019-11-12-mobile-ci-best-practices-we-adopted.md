---
title: "Mobile CI Best Practices We Adopted"
date: 2019-11-12 05:00:00 -0800
categories:
  - Blog
  - General
tags:
  - ci
  - android
  - ios
  - mobile
authors:
  - shiv
---

Mobile CI pipelines have their own quirks.

Practices we adopted:
- Use device farms for E2E testing (Firebase Test Lab, AWS Device Farm)
- Parallelize emulator-based testing on CI runners
- Automate versioning + changelogs on build

Android: used Gradle caching + dependency locking
iOS: setup `fastlane` pipelines with code signing automation

Outcome: faster, more reliable mobile releases across teams.
