---
title: "Running Integration Tests in Docker: Lessons Learned"
date: 2017-03-15 03:00:00 -0700
categories:
  - Tech
  - Containers
tags:
  - docker
  - integration-tests
authors:
  - shiv
---

Integration tests in Docker can catch issues local tests miss.

Setup:
- Compose file with test DB and app container
- Run test suite after boot
- Teardown with `docker-compose down -v`

Helps simulate prod-like envs during CI runs.
