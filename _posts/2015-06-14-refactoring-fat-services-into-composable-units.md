---
title: "Refactoring Fat Services into Composable Units"
date: 2015-06-14 05:40:00 -0700
categories:
  - Tech
  - Microservices
tags:
  - microservices
  - refactoring
authors:
  - shiv
---

We split a massive service into 3 focused modules:
- Command module
- Query module
- Background sync worker

Each is now deployable independently.

Tools we used:
- Spring Boot starter templates
- Maven submodules
- Gradual interface extraction

Key takeaway: Refactoring isn’t rewriting. It’s recomposing.
