---
title: "Designing APIs as Long-Term Contracts"
date: 2013-10-22 02:10:00 -0700
categories:
  - Blog
  - General
tags:
  - api
  - interface-design
  - software-contracts
  - versioning
authors:
  - shiv
---

I had a realization this month while reviewing breaking changes in one of our core APIs: **every API is a contract**, and contracts must be designed with empathy and foresight.

What this means in practice:
- Prefer additive changes; be cautious with removals
- Make versioning a **first-class part** of your design
- Consider the lifecycle of consumers—not just your roadmap

I started incorporating principles from [Joshua Bloch’s API design philosophy](https://www.youtube.com/watch?v=aAb7hSCtvGw) and the early REST maturity models.

This thinking shaped how I later built internal APIs that scaled across teams and versions.
