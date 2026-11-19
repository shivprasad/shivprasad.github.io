---
title: "ASP.Net Custom TreeView and TreeNode .. InvalidCastException"
date: 2009-09-14 09:32:00 -0700
categories:
  - Blog
  - General
tags:
authors:
  - shiv
---

I had to create custom TreeView and TreeNode, and weirdly getting Invalid Cast Exception while I was iterating Nodes and while casting them to my custom TreeNode.... It seems you have to override CreateNode method in your custom TreeView class and return your TreeNode instance from it....
