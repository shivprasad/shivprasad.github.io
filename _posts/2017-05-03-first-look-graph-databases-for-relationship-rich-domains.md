---
title: "First Look: Graph Databases for Relationship-Rich Domains"
date: 2017-05-03 06:30:00 -0700
categories:
  - Tech
  - AI
tags:
  - graph-db
  - neo4j
authors:
  - shiv
---

Relational models often struggle with deep joins.

Graph DBs like Neo4j shine in:
- Social networks
- Recommendations
- Fraud detection

Cypher queries feel expressive:

```
MATCH (a:Person)-[:KNOWS]->(b:Person)
RETURN a.name, b.name

```
