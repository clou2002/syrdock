#JBoss base image
Before you can build this JBoss image, you must download the following software and place it in the noted directory
 - an Oracle jdk like jdk-7u80-linux-x64.tar.gz and put it in the java directory (no need to unzip)
 - jboss-eap-6.3.0.zip -> jboss
 - jboss-eap-6.3.3-patch.zip -> jboss

##Build
IMPORTANT: you have to download the binaries of JBoss and Oracle JDK and put it in place (see .download files inside dockerfiles/).
```
cd 21_eap63
./build.sh
```

##Running JBoss base image
```
cd 21_eap63
./build.sh
```
