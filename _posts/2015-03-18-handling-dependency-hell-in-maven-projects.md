---
title: "Handling Dependency Hell in Maven Projects"
date: 2015-03-18 03:30:00 -0700
categories:
  - Tech
  - Java
tags:
  - dependency-management
  - java
  - maven
authors:
  - shiv
---

This quarter I hit a familiar wall: **dependency hell**.

Multiple transitive versions of Jackson caused random serialization bugs. I fixed it by:
- Using `mvn dependency:tree` to inspect conflicts
- Explicitly excluding conflicting transitive deps
- Creating a central BOM for shared version control

Here's a quick snippet:

```
<dependency>
  <groupId>com.fasterxml.jackson.core</groupId>
  <artifactId>jackson-databind</artifactId>
  <version>2.5.1</version>
</dependency>
<exclusions>
  <exclusion>
    <groupId>org.codehaus.jackson</groupId>
    <artifactId>jackson-mapper-asl</artifactId>
  </exclusion>
</exclusions>

```

Dependency clarity = deployment stability.
