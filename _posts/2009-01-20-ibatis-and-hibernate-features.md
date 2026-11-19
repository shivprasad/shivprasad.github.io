---
title: "iBATIS and Hibernate Features"
date: 2009-01-20 03:04:00 -0800
categories:
  - Tech
  - Java
tags:
  - hibernate
  - ibatis
  - java
---

Recently evaluated Hibernate and iBATIS, there were some good points listed at [this thread](http://www.mail-archive.com/ibatis-user-java@incubator.apache.org/msg01239.html) which I have summarized below with some of my thoughts -

1. iBATIS maps Java Objects to the results of SQL Queries, where as Hibernate maps Java Objects directly to database tables.
2. iBATIS is a "Sql Mapping" implementation of ORM, whereas Hibernate is traditional Object-Relational Mapping.
3. Hibernate automatically generates all the SQL for you and the cache invalidation can be more fine grained. iBATIS is more flexible. You have control over exactly how the SQL queries are written.
4. Use Hibernate if you have mostly standard queries(CRUD, Find by Criteria, etc.) and if you are designing your object model first, then a relational model to support the object model.If you are working with a legacy system or a schema designed by a DBA, iBATIS often makes a better choice.
5. All of the SQL statements used by iBATIS can be stored in XML files outside of Java code, so DBA can easily review them.
6. Also compared to Hibernate, iBATIS is more flexible, has a shorter learning curve, but can take more time to develop and maintain, since you have to write all your queries and if your object model changes you have to go through all your queries and make sure to make all the necessary changes to reflect the changes in your object model.
7. The performance of Hibernate while working with large data sets[complex joins] is not optimal.
8. Hibernate is great when you control the data model, and you let Hibernate do most of the work in the persisting of objects.
9. Unless your existing model is lightweight, adding Hibernate to it is possible, just usually not trivial.
10. Once Hibernate is setup and SQL tuned, productivity gains are very big.
11. iBATIS, will need good DBA or good SQL Developers for SQL tune-ups.
12. iBATIS can be fine-grained optimization for eg. I have a table, this table has a few or dozens of fields, I need to update one of a field, iBATIS is very simple to implement a sql UPDATE using WHERE but with Hibernate, default will update all fields. Though with Hibernate you can control to update only updated fields but that you will have to configure.
13. Similar with select queries where I can choose few columns instead of *, with Hibernate you will get object with all columns. Same applies when I want to update a row in table, with Hibernate I will have to first load that object and then save, two sqls whereas with iBATIS, it would be a single update sql. These are considerations for a interactive database where improving performances is important.
14. iBATIS, SQL maps allow SQL to be fully customized for a specific database. However, these maps do not provide an abstraction from the specific features of the target database.
