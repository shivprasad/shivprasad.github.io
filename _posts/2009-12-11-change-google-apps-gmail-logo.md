---
title: "Change Google Apps - GMail Logo"
date: 2009-12-11 11:00:00 -0800
categories:
  - Tech
  - AI
tags:
  - fluid
  - gmail
  - userscript
---

In Google Apps hosted GMail, when using themes, GMail logo is not changed. If your organization logo is not transparent then it will be distracting for some themes.

I am using Fluid app for GMail and since it supports Userscripts, you can use following userscript.

```
// ==UserScript==
// @name change logo
// @namespace http://fluidapp.com
// @description Changes Google Apps GMail logo.
// @include \*
// @author Someone
// ==/UserScript==
window.addEventListener('load',(function () {
if (window.fluid) {
if(window.parent!=null && window.parent.parent!=null && window.parent.parent.document.getElementById("canvas\_frame")!=null)
{
frmDocument= window.parent.parent.document.getElementById("canvas\_frame").contentDocument;
var gLogo=frmDocument.getElementById(":rh");
if(gLogo!=null && gLogo.tagName=="DIV")
/\*
Use following URL for converting image to base64
http://www.opinionatedgeek.com/dotnet/tools/Base64Encode/Default.aspx
\*/ gLogo.style.setProperty("background-image","url(data:image/image\_type;base64,<>)","important");
}
}
}),true);

```
