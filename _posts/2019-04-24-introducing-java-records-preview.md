---
title: "Introducing Java Records (Preview)"
date: 2019-04-24 01:00:00 -0700
categories:
  - Tech
  - Java
tags:
  - java-14
  - records
authors:
  - shiv
---

Java Records were introduced as a preview feature in JDK 14, but discussions began way earlier.

Why they're exciting:
- Reduce boilerplate for immutable data classes
- Automatically generate `equals`, `hashCode`, `toString`
- Enforce canonical constructor

Example:

```
public record User(String name, int age) {}

```

It felt very Kotlin-esque. This small change has big ergonomic wins for DTO-heavy codebases.
