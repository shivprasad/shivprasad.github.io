---
title: "Moving from Elasticsearch 5 to 6: Migration Notes"
date: 2019-01-16 03:30:00 -0800
categories:
  - Blog
  - General
tags:
  - elasticsearch
  - migrations
  - upgrade
authors:
  - shiv
---

We completed an upgrade from Elasticsearch 5.x to 6.8 this month. It wasn’t seamless, but a few things helped.

Gotchas we hit:
- `_type` deprecation: We had to refactor many mappings to use a single type per index
- Mapping conflicts: dynamic mapping rules changed subtly in v6
- Deprecations in query DSL: especially around `filtered` queries

Tools that helped:
- `elasticsearch-migration` plugin
- Snapshot/restore for index backups
- Integration tests against test clusters

Final result: smoother queries, reduced cluster memory pressure, and better Kibana dashboards.
