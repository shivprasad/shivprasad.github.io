---
title: "Clean Architecture in Spring Boot: Lessons from Refactoring"
date: 2019-01-05 01:00:00 -0800
categories:
  - Tech
  - Java
tags:
  - clean-architecture
  - refactoring
  - spring-boot
authors:
  - shiv
---

Clean Architecture has been gaining popularity, and for good reason. This quarter, we applied it to refactor a mid-sized Spring Boot service that had become a tangled mess of controllers doing too much.

Key principles we implemented:
- Clear separation of domain, application, and infrastructure layers
- Dependency inversion using interfaces for data access and external systems
- Keeping domain logic free of annotations and framework noise

Sample structure:

```
├── domain
├── application
├── infrastructure
└── api

```

Benefits? Easier unit testing, fewer merge conflicts, and a much cleaner mental model.
