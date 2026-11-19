---
title: "Versioned Schemas: The Contract You Can't Ignore"
date: 2014-07-22 05:45:00 -0700
categories:
  - Blog
  - General
tags:
  - compatibility
  - eventing
  - protobuf
  - schema
authors:
  - shiv
---

We started pushing more data through event logs this year. JSON was easy. Until it wasn't.

Problems:
- Extra fields broke consumers
- Enums misaligned across teams
- Schema changes became blockers

We moved to **Protobuf + schema registry**, versioned like APIs, with backward and forward compatibility rules.

![Schema Evolution Lifecycle](https://developers.google.com/protocol-buffers/docs/proto3/images/message-schema.png)

Schema Evolution Lifecycle

Treating schema as a **shared contract** brought more stability than any retry logic ever could.
