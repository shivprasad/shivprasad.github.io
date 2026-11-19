---
title: "Contract Testing with Pact"
date: 2018-08-18 10:00:00 -0700
categories:
  - Blog
  - General
tags:
  - contract-testing
  - pact
authors:
  - shiv
---

When your APIs evolve rapidly, mocking becomes unreliable. That’s where [Pact](https://docs.pact.io/) helps.

Pact introduces consumer-driven contracts: your client defines expectations, and the provider verifies against them.

Key advantage:
- Prevents unintentional breakage
- Promotes API stability across teams

Example pact snippet:

```
{
  "provider": { "name": "UserService" },
  "consumer": { "name": "Dashboard" },
  "interactions": [...]
}

```

We integrated Pact with CI to reject builds that broke published contracts. It raised trust across services.
