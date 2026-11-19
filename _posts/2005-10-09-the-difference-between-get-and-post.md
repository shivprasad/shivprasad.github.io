---
title: "The difference between GET and POST"
date: 2005-10-09 20:20:00 -0700
categories:
  - Blog
  - General
tags:
---

I was hunting the web for the difference between HTML form submission methods**GET** and **POST**.This is what my understanding is.:)

## The Basic Difference

**GET** should be used if and only if there are no side effects.Many database searches have no visible side-effects and make ideal applications of query forms.The **GET** method is designed for getting information (a document, a chart, or the results from a database query).**POST** method is designed for posting information (a credit card number, some new chart data, or information that is to be stored in a database).If the service associated with the processing of a form has side effects (for example, modification of a database or subscription to a service), the method should be **POST**.

## The Form Encoding Difference

In terms of form data encoding, the difference between METHOD="GET" (the default) and METHOD="POST" is -

- If the method is "get" - -, the user agent takes the value of action, appends a ? to it, then appends the form data set, encoded using the *application/x-www-form-urlencoded* content type. The user agent then traverses the link to this URI. In this scenario, form data are restricted to ASCII codes.
- If the method is "post" --, the user agent conducts an HTTP post transaction using the value of the action attribute and a message created according to the content type specified by the enctype attribute.The **POST** can be submitted using either *multipart/form-data* or *application/x-www-form-urlencoded* (the default)

A "GET" request is often cacheable, whereas a "POST" request can hardly be.
The user could bookmark **GET** requests(say a search result) or cut&paste it for later use (e.g. to be E-mailed or put into one's own HTML document after some editing).Browsers typically will (indeed "should") caution their users if they are about to resubmit a **POST**request.

## Server Side Mechanics

In terms of mechanics in CGI scripts, they differ in how parameters are passed to the
CGI script. In the case of a POST request, form data is passed on
STDIN, so the script should read from there (the number of bytes to be
read is given by the Content-length header). In the case of GET, the
data is passed in the environment variable QUERY_STRING. The content-type
(application/x-www-form-urlencoded) is identical for GET and POST requests.
For reasons explained above, one should normally use METHOD="POST" if and only if the form submission may cause changes.There are libraries of subroutines (e.g. Perl functions) which allow one to write scripts in a manner which works both for METHOD="GET" and METHOD="POST".

## Maximum URL Length

Because GET requests theoretically shouldn't need to send large amounts of information, some servers limit the length of URLs and query strings to about 240 characters.
Internet Explorer has a maximum uniform resource locator (URL) length of 2,083 characters, with a maximum path length of 2,048 characters. This limit applies to both POST and GET request URLs.
If you are using the GET method, you are limited to a maximum of 2,048 characters (minus the number of characters in the actual path, of course).
POST, however, is not limited by the size of the URL for submitting name/value pairs, because they are transferred in the header and not the URL.
