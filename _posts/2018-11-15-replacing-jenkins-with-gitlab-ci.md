---
title: "Replacing Jenkins with GitLab CI"
date: 2018-11-15 06:15:00 -0800
categories:
  - Blog
  - General
tags:
  - ci
  - gitlab
  - pipeline
authors:
  - shiv
---

After years of Jenkins pipelines, we tested GitLab CI for internal services. The `.gitlab-ci.yml` model was declarative and powerful.

Benefits:
- Reduced plugin sprawl
- Pipeline-as-code was intuitive
- Built-in Docker image registry

Migration took time but was worth it. We ended up with cleaner, faster pipelines and tighter VCS integration.
