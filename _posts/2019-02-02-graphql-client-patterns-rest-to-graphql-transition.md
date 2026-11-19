---
title: "GraphQL Client Patterns: REST to GraphQL Transition"
date: 2019-02-02 05:00:00 -0800
categories:
  - Blog
  - General
tags:
  - apollo
  - frontend
  - graphql
authors:
  - shiv
---

We began adopting GraphQL for some internal APIs, and client design emerged as a key concern.

Useful patterns:
- Fragments to isolate UI-level concerns
- Co-location of queries with components (React + Apollo)
- Batching and caching with Apollo Client

Challenges:
- Handling versioning without breaking contract
- Too much flexibility sometimes caused unexpected N+1 calls

Migration Tip: Don’t try to rewrite everything. Create a BFF layer that wraps legacy REST and new GraphQL gradually.
