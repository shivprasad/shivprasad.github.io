---
title: "Docker Multi-Stage Builds: Smaller, Cleaner Images"
date: 2017-05-10 02:00:00 -0700
categories:
  - Tech
  - Containers
tags:
  - containers
  - docker
authors:
  - shiv
---

Docker 17.05 introduced multi-stage builds.

Benefits:
- No build tools in final image
- Clear separation of stages
- Smaller image sizes

Example:

```
FROM maven:3.5-jdk-8 as builder
WORKDIR /app
COPY . .
RUN mvn clean package

FROM openjdk:8-jre
COPY --from=builder /app/target/app.jar /app.jar
CMD ["java", "-jar", "/app.jar"]

```
