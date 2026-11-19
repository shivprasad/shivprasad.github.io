---
title: "Gran Paradiso Alpha 1 - Firefox 3.0"
date: 2006-12-10 22:30:00 -0800
categories:
  - Blog
  - General
tags:
---

![The image â€œhttp://www.mozilla.org/projects/firefox/3.0a1/releasenotes/releasenotes-granparadiso-alpha1.pngâ€ cannot be displayed, because it contains errors.](http://www.mozilla.org/projects/firefox/3.0a1/releasenotes/releasenotes-granparadiso-alpha1.png)

The image â€œhttp://www.mozilla.org/projects/firefox/3.0a1/releasenotes/releasenotes-granparadiso-alpha1.pngâ€ cannot be displayed, because it contains errors.

Gecko 1.9 Alpha 1 introduces several new features which can be tested by using Gran Paradiso Alpha 1:

- [Cairo](http://wiki.mozilla.org/Cairo) is now being used as the default graphics library, affecting all graphic and text rendering
- [Cocoa Widgets](http://wiki.mozilla.org/Mac:Cocoa_Widgets) are now used in OS X builds
- An updated [threading model](http://wiki.mozilla.org/XPCOM:nsIThreadManager)
- Changes to how DOM events are dispatched (see [bug 234455](https://bugzilla.mozilla.org/show_bug.cgi?id=234455))
- Changes to how
- Changes to how [web pages are painted](http://weblogs.mozillazine.org/roc/archives/2005/11/frame_display_lists.html)
- New SVG elements and filters, and improved SVG specification compliance

Some of the changes in Gecko 1.9 Alpha 1 will affect the web and platform compatibility of Gran Paradiso Alpha 1:

- Windows 95, Windows 98 and Windows ME are no longer supported platforms
- OS X 10.2 is no longer supported, and OS X 10.3.9 or higher is recommended
- Moving DOM nodes between documents now requires a call to importNode or adoptNode as per the [DOM specification](http://www.w3.org/TR/2000/CR-DOM-Level-2-20000510/core.html#ID-184E7107).

[Visit](http://www.mozilla.org/projects/firefox/3.0a1/releasenotes/)
