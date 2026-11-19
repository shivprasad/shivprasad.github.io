---
title: "Debugging Thread Leaks in Java Applications"
date: 2016-12-22 03:15:00 -0800
categories:
  - Tech
  - Java
tags:
  - java
  - thread-leak
authors:
  - shiv
---

Thread leaks = hidden production killers.

What helped:
- Thread dumps via `jstack`
- Analyzing executor pools
- Setting thread naming conventions

Always clean up thread pools in shutdown hooks.
