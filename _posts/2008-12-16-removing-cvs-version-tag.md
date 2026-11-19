---
title: "Removing CVS Version Tag"
date: 2008-12-16 22:30:00 -0800
categories:
  - Blog
  - General
tags:
  - cvs
  - eclipse
---

I use [RAD 7.0](http://www.ibm.com/software/awdtools/studioappdev/)  IDE for the development. During current release, one of the project got tagged by mistake.
Eclipse does not support removing of CVS tag.Below is how I was able to remove a tag from module.
[sourcecode language='sh']
$cvs -d :ssh:<>@<>:<> login
[/sourcecode]
The above will login to the CVS. To remove a tag,
[sourcecode language='sh']
$cvs -d :ssh:<>@<>:<> rtag -d <> â€œ<>â€
[/sourcecode]
You should see "cvs rtag: Untagging <>" as above command output. Done.
Technorati Tags: [eclipse](http://technorati.com/tag/eclipse), [cvs](http://technorati.com/tag/cvs), [tag](http://technorati.com/tag/tag), [remove](http://technorati.com/tag/remove), [rtag](http://technorati.com/tag/rtag), [rad](http://technorati.com/tag/rad), [rational application developer](http://technorati.com/tag/rational%20application%20developer)
