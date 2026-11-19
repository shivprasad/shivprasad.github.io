---
title: "Introducing Auto-Scaling Event Drivers for Background Processing"
date: 2017-11-27 06:00:00 -0800
categories:
  - Blog
  - General
tags:
  - event-driven
  - scaling
authors:
  - shiv
---

Event-driven processing gives you decoupling. But scaling workers dynamically is often neglected.

We wrote a wrapper to:
- Monitor queue depth in Kafka
- Trigger horizontal pod autoscaler adjustments
- Handle warmup and cooldown periods intelligently

This reduced costs significantly during off-peak and absorbed traffic spikes more gracefully.
