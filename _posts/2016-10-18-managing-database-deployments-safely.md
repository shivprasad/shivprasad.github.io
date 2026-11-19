---
title: "Managing Database Deployments Safely"
date: 2016-10-18 04:00:00 -0700
categories:
  - Blog
  - General
tags:
  - flyway
  - liquibase
  - schema-migration
authors:
  - shiv
---

Breaking production due to schema changes? We’ve all been there.

Recommendations:
- Add columns first, backfill async, remove later
- Use tools like Flyway or Liquibase
- Keep schema and code versioned together

Always test rollback paths.
