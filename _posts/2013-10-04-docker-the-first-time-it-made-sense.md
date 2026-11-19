---
title: "Docker: The First Time It Made Sense"
date: 2013-10-04 04:30:00 -0700
categories:
  - Tech
  - Containers
tags:
  - ci/cd
  - containers
  - docker
  - virtualization
authors:
  - shiv
---

October 2013 was when I finally *got* Docker.

While containers had existed before, Docker introduced a developer-friendly interface that made packaging, shipping, and running apps feel seamless.

The key ideas:
- Containers are **lightweight, fast, and portable**
- Build once, run anywhere wasn’t just marketing—it actually worked
- Dev/prod parity became more achievable

Docker 0.7 released around this time added [AUFS](https://en.wikipedia.org/wiki/Aufs), improving image layering and file system support.

It changed how I thought about **build pipelines, staging, and rollback strategies**.
