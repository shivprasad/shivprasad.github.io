---
title: "Logstash, Finally Done Right"
date: 2014-04-18 09:10:00 -0700
categories:
  - Tech
  - Observability
tags:
  - elk
  - devops
  - logging
  - logstash
authors:
  - shiv
---

[ThoughtWorks Radar](https://www.thoughtworks.com/radar/tools/logstash) called out **Logstash** this quarter, and it deserved it.

We adopted Logstash to clean and route logs from multiple systems:
- App logs
- Job queues
- Ingress/egress metrics

The pipeline-based config was a game-changer.

What I liked:
- Easy to onboard new formats
- Rich plugin ecosystem
- Paired beautifully with Kibana for dashboarding

![Logstash Pipeline](https://logz.io/wp-content/uploads/2021/06/Logstash_Pipeline_Architecture.png)

Logstash Pipeline

Logging went from debugging nightmare to a core engineering feedback loop.
