---
title: "Debugging Intermittent JVM Crashes with Heap Dumps"
date: 2015-12-19 06:30:00 -0800
categories:
  - Tech
  - Java
tags:
  - heapdump
  - java
authors:
  - shiv
---

Sporadic crashes are always tough. We finally traced ours using heap dumps and MAT.

Steps:
- Enable `-XX:+HeapDumpOnOutOfMemoryError`
- Analyze dump using [Eclipse MAT](https://www.eclipse.org/mat/)
- Identify retained sets and suspect dominators

MAT helped visualize object retention trees, revealing a listener registration leak.

It’s like archaeology — but with memory graphs.
