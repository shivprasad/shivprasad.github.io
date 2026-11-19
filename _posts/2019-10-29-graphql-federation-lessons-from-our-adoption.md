---
title: "GraphQL Federation: Lessons from Our Adoption"
date: 2019-10-29 05:00:00 -0700
categories:
  - Blog
  - General
tags:
  - federation
  - graphql
authors:
  - shiv
---

We began adopting Apollo Federation across multiple services.

What worked:
- Schema composition helped with ownership boundaries
- Clear separation between gateway and service-level resolvers
- SDL-first with codegen improved type safety

Gotchas:
- N+1 query risks across services
- Difficulty debugging deeply nested queries

Add caching and batching early. And monitor your query shapes.
