---
title: "Debugging Memory Leaks in Java NIO Systems"
date: 2016-09-10 04:45:00 -0700
categories:
  - Tech
  - Java
tags:
  - memory-leak
  - nio
authors:
  - shiv
---

One of our systems with heavy NIO usage showed gradual memory leaks.

Root cause:
- Direct byte buffers not released properly
- Missing `Cleaner` references in old JDK

Tools used:
- `jcmd` and `jmap`
- Eclipse MAT
- Manual tracking of buffer allocations

Lesson: Off-heap memory is not magic — it leaks too.
