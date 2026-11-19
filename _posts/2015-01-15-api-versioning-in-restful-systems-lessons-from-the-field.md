---
title: "API Versioning in RESTful Systems: Lessons from the Field"
date: 2015-01-15 03:00:00 -0800
categories:
  - Blog
  - General
tags:
  - design
  - eb1a
  - rest
  - versioning
authors:
  - shiv
---

Versioning is hard. But deprecating unversioned APIs? Even harder.

This quarter, we migrated a set of internal APIs to a versioned model using URI-based versioning (`/v1/` style). Key lessons:
- Include version negotiation in contract discussions
- Avoid URI pollution with semver unless truly needed
- Backward compatibility ≠ never change

Relative stability, clear upgrade paths, and automatic contract testing helped streamline our rollout.

![API Versioning](https://miro.medium.com/v2/resize:fit:720/format:webp/1*mpzqA6gQ45b_9iDDoAogFA.png)

API Versioning
