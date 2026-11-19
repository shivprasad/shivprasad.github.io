---
title: "ZooKeeper vs etcd: Choosing the Right Coordination Service"
date: 2015-08-05 02:00:00 -0700
categories:
  - Blog
  - General
tags:
  - coordination
  - etcd
  - zookeeper
authors:
  - shiv
---

We evaluated ZooKeeper and etcd for coordination needs across distributed systems.

Criteria:
- Consistency under partition
- Ease of use and tooling
- Integration with service discovery

Findings:
- ZooKeeper has strong consistency, mature support (Curator)
- etcd is lighter, easier to work with for modern stacks
- etcd’s gRPC/HTTP API = big win

We eventually chose etcd for its simplicity, but ZooKeeper still shines in legacy-heavy environments.
