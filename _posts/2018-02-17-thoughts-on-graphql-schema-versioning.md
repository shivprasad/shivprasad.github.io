---
title: "Thoughts on GraphQL Schema Versioning"
date: 2018-02-17 03:00:00 -0800
categories:
  - Blog
  - General
tags:
  - api
  - graphql
authors:
  - shiv
---

As GraphQL picked up adoption, schema versioning surfaced as a practical challenge.

REST gave us `/v1/`, `/v2/` endpoints. But with GraphQL, you only get one endpoint — so how do you evolve a schema without breaking clients?

I explored:
- Deprecation directives (`@deprecated`)
- Federated schemas for isolated change
- Schema linting before merging

In the end, what worked best was a client-usage analysis and traffic-aware evolution. If a field wasn’t being used, we removed it after two sprints of deprecation.

GraphQL offers flexibility, but you need discipline in schema governance.
