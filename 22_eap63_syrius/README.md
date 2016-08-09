#Syrius Image
Before you can build this image, make sure you have built the JBoss base image described in the previous steps.
You must extract an official Syrius tar to 22_eap63_syrius/syrius/software.

##Build the image
```
cd 22_eap63_syrius
./build.sh
```

##Run Syrius
Make sure you have the credentials of your running Syrius database ready. The database schema must have the exact same release as the Syrius software you want to run. If this is not the case, use dbupdate/refreshdb to update your database.

To ease startup of Syrius components there are some helper scipts in the *scripts* directory


###Application Server
```
./start_app.sh
or
docker run -d --name syr_app -p 42705:42705 -p 42707:42707 -p 9990:9990 clou/syr:3_06_HEAD
<<<<<<< HEAD
```
###UTC Server
```
./start_app.sh
=======
or to pass your database credentials
docker run -d --name syr_app -p 42705:42705 -p 42707:42707 -p 9990:9990 --env DB_JDBC_URL="jdbc:oracle:thin:@//myhost:myport/myservicename" clou/syr:3_06_HEAD
```
####Test
- [Version Servlet](http://localhost:42705/syrius/version)

###UTC Server
Before starting UTC, wait for de Version Servlet to be ready.
```
./start_utc.sh
>>>>>>> 6c7b4eafd0de34023d0594a9c847ab49ab732d9b
or
docker run -d --name syr_utc --link syr_app:syrnet -p 42703:42703 clou/syr:3_06_HEAD /opt/jboss/syrius/bin/utc_start
```
###Elasticsearch
TODO
###JPS Client
```
./startclient.sh
```
###All together
TODO docker-compose up
