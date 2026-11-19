---
title: "Kotlin in Backend Services: A Year in"
date: 2018-10-12 05:30:00 -0700
categories:
  - Tech
  - Java
tags:
  - backend
  - java
  - kotlin
authors:
  - shiv
---

Kotlin wasn’t just for Android anymore. Over the past year, we had multiple production backend services running on Kotlin.

What worked:
- Concise null-safe syntax reduced NPEs
- Data classes made DTO modeling clean
- Coroutines provided a readable async model

Some challenges:
- Reflection-heavy libraries needed tuning
- DI with Koin felt lighter than Dagger, but less powerful than Guice

Overall, it made backend development more fun and expressive without sacrificing JVM strengths.
