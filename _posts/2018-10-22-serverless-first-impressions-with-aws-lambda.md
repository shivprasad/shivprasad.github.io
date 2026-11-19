---
title: "Serverless First Impressions with AWS Lambda"
date: 2018-10-22 02:00:00 -0700
categories:
  - Blog
  - General
tags:
  - aws
  - lambda
  - serverless
authors:
  - shiv
---

I tried serverless in earnest this quarter. AWS Lambda was the entry point — triggered by S3 events, SNS topics, or API Gateway.

Pros:
- Zero infra management
- Great for bursty workloads
- Tight integration with other AWS services

Gotchas:
- Cold starts on VPC-attached Lambdas
- Local development/debugging friction
- Observability required CloudWatch gymnastics

Use case: we built a log-parsing pipeline that fanned out processing using SNS + Lambda + DynamoDB.

Still not a silver bullet, but a powerful addition to the toolbox.
