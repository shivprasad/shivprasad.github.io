---
title: "Why Not All Microservices Should Be Services"
date: 2014-10-06 03:00:00 -0700
categories:
  - Tech
  - Microservices
tags:
  - microservices
  - modular-monolith
  - scalability
  - team-boundaries
authors:
  - shiv
---

In recent months, I’ve seen an interesting trend: teams breaking things into microservices too early.

We tried that, and paid the price:
- Increased network hops
- More failure points
- CI/CD complexity

We refactored some of those “microservices” into **modular monoliths** instead — still decoupled in code, but deployed as a unit.

![Monolith vs Services](https://martinfowler.com/bliki/images/monolithFirst/microservice-monolith.png)

Monolith vs Services

It’s not about the number of services. It’s about *how* you isolate logic and *why*.
