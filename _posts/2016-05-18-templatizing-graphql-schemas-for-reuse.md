---
title: "Templatizing GraphQL Schemas for Reuse"
date: 2016-05-18 03:45:00 -0700
categories:
  - Blog
  - General
tags:
  - graphql
  - schema-design
authors:
  - shiv
---

When working on federated GraphQL systems, reusing schema fragments becomes crucial.

Tips:
- Use custom schema printers to extract and reuse
- Modularize common types like `PageInfo`, `Error`, `Metadata`
- Explore schema stitching if federation feels like overkill
