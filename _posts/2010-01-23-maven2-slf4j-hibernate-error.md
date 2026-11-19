---
title: "maven2, slf4j, hibernate error"
date: 2010-01-23 08:22:00 -0800
categories:
  - Tech
  - Java
tags:
  - hibernate
  - mvn
  - slf4j
---

Got following exception while executing "mvn test"

> java.lang.IllegalAccessError: tried to access field org.slf4j.impl.StaticLoggerBinder.SINGLETON from class org.slf4j.LoggerFactory
> 

My pom.xml had following entry wrt slf4j -

```
org.slf4j
slf4j-log4j12
1.5.6

```

Adding slf4j api dependency did the trick -

```
org.slf4j
slf4j-api
1.5.6

```
