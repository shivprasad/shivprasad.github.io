---
title: "Maven, dbdeploy, HSQLDB without Ant"
date: 2010-01-31 14:59:00 -0800
categories:
  - Tech
  - Java
tags:
  - ant
  - dbdeploy
  - maven
---

Believe me, integrating Maven and dbdeploy is a pain using Ant. For some weird reasons, dbdeploy ant task was causing maven build to crash.
So tried to integrate dbdeploy with maven without ant on my Snow Leopard -
You will need following jars -
dbdeploy-cli-3.0M2.jar
hsqldb-1.8.0.7.jar
keep above jars in dir "db" in same dir of pom.xml and keep your dbdeploy sql scripts in dir "db/scripts". This will look like -

```
|-db
|----lib
|-------dbdeploy-cli-3.0M2.jar
|-------hsqldb-1.8.0.7.jar
|----scripts
|-------createSchemaVersionTable.sql
|-pom.xml

```

Next configure following Maven plugins -

```
org.codehaus.mojo
sql-maven-plugin
1.1

hsqldb
hsqldb
1.8.0.7

${test.jdbc.driverClassName}
${test.jdbc.url}
${test.jdbc.username}
${test.jdbc.password}

create-change-log
process-test-sources

execute

${basedir}/db/scripts/createSchemaVersionTable.sql

apply-db-changes
process-test-classes

execute

${basedir}/target/consolidated\_script.sql

```

createSchemaVersionTable.sql is part of dbdeploy distribution. Copy HSQLDB version.
And the following

```
org.codehaus.mojo
exec-maven-plugin
1.1

dbdeploy
test-compile

exec

java
${basedir}/db

-cp ${test.hsql.jar}:lib/dbdeploy-cli-3.0M2.jar com.dbdeploy.CommandLineTarget -U ${test.jdbc.username} -D ${test.jdbc.driverClassName} -u ${test.jdbc.url.escaped} -d ${test.dbdeploy.dbms.type} -o ${basedir}/target/consolidated\_script.sql -s scripts/

```

Following are the important maven properties that are to be set -

```
org.hsqldb.jdbcDriver
jdbc:hsqldb:file:${basedir}/target/testdb;shutdown=true
jdbc:hsqldb:file:${basedir}/target/testdb\\;shutdown=true
sa

hsql
lib/hsqldb-1.8.0.7.jar

```

How it works -
We are using dbdeploy command line interface to achieve integration. The HSQLDB is used in a file mode which is evident by test.jdbc.url, since maven exec task executes by using bash semi-colon used in jdbc url needs to be escaped, thats the reason for defining test.jdbc.url.escaped property.
The sql-maven-plugin's execution "create-change-log" is configured to run after phase "process-test-sources", which creates change log table which is required by dbdeploy.
The exec-maven-plugin's execution "dbdeploy" is configured to run after phase "test-compile", executes dbdeploy command line interface, creates "${basedir}/target/consolidated_script.sql" which contains sql changes to be applied.
The sql-maven-plugin's execution "apply-db-changes" is configured to run after phase "process-test-classes", which applies consolidated change log script.
Hope it helps somebody..
