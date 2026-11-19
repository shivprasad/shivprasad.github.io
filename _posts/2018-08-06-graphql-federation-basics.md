---
title: "GraphQL Federation Basics"
date: 2018-08-06 02:00:00 -0700
categories:
  - Blog
  - General
tags:
  - federation
  - schema
authors:
  - shiv
---

As GraphQL services scaled, managing monolithic schemas became unmanageable. That's where [Apollo Federation](https://www.apollographql.com/docs/federation/) entered.

Federation enables:
- Composable schemas across services
- Explicit ownership per domain
- Seamless joins via `@key`, `@external` directives

Example:

```
type Product @key(fields: "id") {
  id: ID!
  name: String
}

```

Each service owns its slice. Gateway stitches them together.

This aligned well with our microservices and allowed independent evolution of APIs.
