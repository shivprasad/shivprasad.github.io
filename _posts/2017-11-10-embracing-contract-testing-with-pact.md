---
title: "Embracing Contract Testing with Pact"
date: 2017-11-10 07:45:00 -0800
categories:
  - Blog
  - General
tags:
  - contract-testing
  - pact
authors:
  - shiv
---

Working with microservices means dealing with evolving interfaces. Pact provided a much-needed bridge between frontend and backend teams.

We used it to:
- Define consumer expectations early
- Automate provider verification
- Detect breaking changes before deployment

Pact Broker helped coordinate versioning across services. It wasn't perfect — flaky CI builds were common — but the benefits outweighed the friction.

Bonus: it reduced back-and-forth debugging by a lot.
