---
title: "Safari and WebDriver: A Testing Frustration Story"
date: 2017-05-19 10:00:00 -0700
categories:
  - Blog
  - General
tags:
  - safari
  - webdriver
authors:
  - shiv
---

Cross-browser testing is tricky — Safari made it worse.

Observations:
- SafariDriver has quirks vs ChromeDriver
- Popups and alerts are problematic
- Debug logs are minimal

Eventually, settled on remote testing via SauceLabs for Mac-specific cases.
