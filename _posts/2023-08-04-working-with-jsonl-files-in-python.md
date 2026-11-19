---
title: "Working with JSONL Files in Python"
date: 2023-08-04 03:00:00 -0700
categories:
  - Blog
  - General
tags:
  - data
  - jsonl
authors:
  - shiv
---

JSONL (JSON Lines) is underrated:

- Great for streaming structured logs
- Easy to parse with low memory overhead
- One object per line = grep-friendly

Python snippet to load:

```
import json
with open("file.jsonl") as f:
    for line in f:
        print(json.loads(line))

```
