---
title: "Simplifying Gradle Build Scripts"
date: 2016-06-27 05:10:00 -0700
categories:
  - Blog
  - General
tags:
  - build-automation
  - gradle
authors:
  - shiv
---

Gradle is powerful, but can get verbose fast.

Tricks:
- Use `ext` blocks for version centralization
- Profile builds with `--profile` and analyze bottlenecks
- Write reusable buildSrc plugins

![Gradle Sample](https://docs.gradle.org/current/userguide/img/intro-single-project-build.png)

Gradle Sample

Simple builds scale better.
