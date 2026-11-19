---
title: "Profiling Spring Boot Applications with VisualVM"
date: 2015-01-30 06:45:00 -0800
categories:
  - Tech
  - Java
tags:
  - profiling
  - spring-boot
  - visualvm
authors:
  - shiv
---

I was debugging a high CPU usage issue in one of our Spring Boot services. Turned out to be an accidental infinite loop triggered by malformed input.

To catch it, I used [VisualVM](https://visualvm.github.io/):
1. Start your Spring Boot app with remote debug flags:

```
java -Dcom.sun.management.jmxremote -jar myservice.jar

```

1. Connect via VisualVM and inspect CPU sampling
2. Sort by method usage, identify hotspots

Console output:

```
Method           | Time   | Invocations
loopProcessor()  | 97.2%  | 2,193,840

```

Lesson: Always watch for unbounded iterations, especially when processing user input.
