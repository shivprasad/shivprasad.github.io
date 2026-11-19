---
title: "VM Lifecycle Automation with SaltStack"
date: 2015-12-09 04:00:00 -0800
categories:
  - Blog
  - General
tags:
  - automation
  - saltstack
authors:
  - shiv
---

We piloted [SaltStack](https://saltproject.io) to handle VM provisioning and configuration.

Benefits:
- Easy YAML syntax for states
- Powerful remote execution
- Strong support for event-driven automation

Example state:

```
apache:
  pkg.installed: []
  service.running:
    - enable: True

```

Lightweight and scriptable — worked great for our scale.
