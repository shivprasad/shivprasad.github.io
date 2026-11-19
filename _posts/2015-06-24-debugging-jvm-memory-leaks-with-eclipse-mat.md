---
title: "Debugging JVM Memory Leaks with Eclipse MAT"
date: 2015-06-24 04:00:00 -0700
categories:
  - Tech
  - Java
tags:
  - eclipse-mat
  - jvm
  - memory
authors:
  - shiv
---

Hit a nasty memory leak in our backend. Heap dumps were huge. Enter [Eclipse Memory Analyzer Tool](https://www.eclipse.org/mat/).

It helped us:
- Analyze heap retention paths
- Identify orphaned caches
- Fix static collections growing forever

Heap histograms showed:

```
java.util.HashMap  - 3.4 GB
byte[]             - 2.1 GB

```

Lesson: Don't guess memory usage. Profile it.
