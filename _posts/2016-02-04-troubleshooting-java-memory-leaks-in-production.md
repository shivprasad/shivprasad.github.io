---
title: "Troubleshooting Java Memory Leaks in Production"
date: 2016-02-04 03:15:00 -0800
categories:
  - Tech
  - Java
tags:
  - java
  - memory-leak
authors:
  - shiv
---

When your app starts eating up heap, it’s time to break out the diagnostics.

Steps:
- Collect heap dumps with `-XX:+HeapDumpOnOutOfMemoryError`
- Use Eclipse MAT to analyze retained sets
- Identify leak suspects and dominator trees

In our case, an executor service wasn’t being shut down — held on to task references.

Memory leaks love long-lived services. Clean up after yourself.
