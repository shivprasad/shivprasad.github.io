---
title: "Radar Comment: Deployable Libraries as Contracts"
date: 2015-05-08 02:45:00 -0700
categories:
  - Blog
  - General
tags:
  - api
  - contracts
  - thoughtworks-radar
authors:
  - shiv
---

[Radar Q2 2015](https://www.thoughtworks.com/radar/techniques/deployable-libraries) pushed **Deployable Libraries** as a collaboration strategy. Totally agree.

Instead of coordinating API updates, we:
- Encapsulate contracts as versioned jars
- Deliver shared validation logic and clients
- Ensure semantic versioning and changelog updates

Works beautifully for federated teams. Consumers just update a dependency.
