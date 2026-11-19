---
title: "The Danger of Shared Databases in Microservice Design"
date: 2014-04-07 04:40:00 -0700
categories:
  - Tech
  - Microservices
tags:
  - data-boundaries
  - decoupling
  - microservices
  - ownership
authors:
  - shiv
---

I’ve seen microservice efforts collapse because teams couldn’t let go of shared databases.

Here’s what went wrong:
- Coupled data models → fragile services
- Shared tables → ownership ambiguity
- Cross-service joins → impossible to scale

We fixed this by:
- Assigning strict ownership per bounded context
- Exposing only APIs and asynchronous events
- Moving reporting to an async materialized layer

![Service and DB Mapping](https://martinfowler.com/articles/microservices/images/microservice-boundaries.png)

Service and DB Mapping

Microservices need boundaries. And boundaries need enforcement.
