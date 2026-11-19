---
title: "Profiling with Java Flight Recorder"
date: 2018-07-26 04:15:00 -0700
categories:
  - Tech
  - Java
tags:
  - jvm
  - performance
  - profiling
authors:
  - shiv
---

Tuning JVM apps got a lot easier with [Java Flight Recorder](https://docs.oracle.com/javase/9/jfapi/what-is-jfr.htm). Instead of invasive profilers, we could now trace hotspots with minimal overhead.

Key wins:
- Identify GC pauses and allocation spikes
- Analyze lock contention
- Correlate thread dumps with memory usage

Trigger recording via:

```
jcmd <pid> JFR.start name=debug duration=60s filename=recording.jfr

```

And view with Java Mission Control (JMC).

JVM observability keeps getting better.
