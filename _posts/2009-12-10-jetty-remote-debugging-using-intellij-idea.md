---
title: "Jetty Remote Debugging using IntelliJ IDEA"
date: 2009-12-10 14:28:00 -0800
categories:
  - Tech
  - Java
tags:
  - java
---

Recently wanted to remotely debug Jetty instance, which was using **mvn jetty:run.**

Using following MAVEN_OPTS worked for me -

> $ export MAVEN_OPTS="-Xms256m -Xmx512m -agentlib:jdwp=transport=dt_socket,address=7848,server=y,suspend=n"
> 

After setting above executed -

> mvn jetty:run
> 

Then configured IDEA Remote Server by connecting to server on above configured port 7848
