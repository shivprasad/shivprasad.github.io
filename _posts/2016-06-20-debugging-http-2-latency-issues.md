---
title: "Debugging HTTP/2 Latency Issues"
date: 2016-06-20 02:50:00 -0700
categories:
  - Blog
  - General
tags:
  - http2
  - latency
authors:
  - shiv
---

HTTP/2 promised better performance, but we hit some odd latency spikes.

Learnings:
- Head-of-line blocking still matters in some browsers
- Prioritization frames not always honored
- Wireshark + `nghttp` tool helped investigate frames

HTTP/2 is still maturing. Monitor, then optimize.
