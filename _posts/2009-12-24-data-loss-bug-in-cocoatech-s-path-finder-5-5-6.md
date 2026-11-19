---
title: "Data Loss Bug in Cocoatech's Path Finder 5.5.6"
date: 2009-12-24 00:19:00 -0800
categories:
  - Blog
  - General
tags:
  - apple
  - bug
  - cocoatech
  - osx
  - path-finder
---

Cocoatech's Path Finder is a great application. I am trying it out for some time now. I have noticed following bug couple of times.
If you have a file of more than 4gb stored on file system of type "Mac OS Extended" , and if you try to move it to a FAT32 partition, it fails.
Which is fine since max file size on FAT32 file system is 4gb. What is frustrating is that Path Finder doesn't tell you this that the file move operation is failed. On top of it, it will remove file stored on "Mac OS Extended" file system, thinking the file move operation was successful.
Uhhh....big thumbs down... I wish they fix this problem....
