---
title: "Cloud Cost Optimization Tactics That Worked"
date: 2019-10-18 07:00:00 -0700
categories:
  - Blog
  - General
tags:
  - aws
  - cost-optimization
authors:
  - shiv
---

We hit a cloud bill spike — and it triggered a deep audit.

Wins:
- Moved to spot instances for stateless workloads
- S3 lifecycle policies cleaned up old logs
- Consolidated VPC endpoints

Tip: tag aggressively and review cost by tag monthly. A single forgotten NAT gateway can cost a lot.

Tool: [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/) was surprisingly effective.
