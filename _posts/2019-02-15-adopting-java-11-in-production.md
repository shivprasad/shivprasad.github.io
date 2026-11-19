---
title: "Adopting Java 11 in Production"
date: 2019-02-15 02:15:00 -0800
categories:
  - Tech
  - Java
tags:
  - java-11
  - migrating
  - spring-boot
authors:
  - shiv
---

With Java 11 being the next LTS, we finally made the switch.

Steps we followed:
- Upgraded build toolchain (Maven/Gradle)
- Verified compatibility of 3rd party libraries
- Switched from CMS GC to G1GC and later ZGC for select services

Benefits:
- Better memory handling under G1GC
- Support for `var`, HTTP Client API, and modules (experimentally)

Note: Spring Boot 2.1+ works well with Java 11.
