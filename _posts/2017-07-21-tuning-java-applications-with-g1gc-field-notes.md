---
title: "Tuning Java Applications with G1GC: Field Notes"
date: 2017-07-21 02:00:00 -0700
categories:
  - Tech
  - Java
tags:
  - g1gc
  - gc
  - performance
authors:
  - shiv
---

G1GC is now the default in Java 9. Key tuning insights:

- `MaxGCPauseMillis` is your lever for latency
- Watch survivor space promotion rate
- Use GC logs + GCViewer or GCEasy for analysis

We cut pause times by ~40% with right configs.
