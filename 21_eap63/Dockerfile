# LICENSE CDDL 1.0 + GPL 2.0
#
# Copyright (c) 2016 Adcubum AG and/or its affiliates. All rights reserved.
# 
# Adcubum AG DOCKERFILES PROJECT
# --------------------------
# This Dockerfile extends the jboss base image built under jboss/base with tag name 'latest'
#
# It will deploy any package defined in APP_PKG_FILE located in APP_PKG_LOCATION
# into the DOMAIN_HOME with name defined in APP_NAME
# It will install Oracle JDK 7, JBoss EAP 6.3.0 and patch 6.3.3
#
# HOW TO BUILD THIS IMAGE
# -----------------------
# Run: 
#      $ docker build -t clou/syr:eap6jdk7 .
#

# Pull base image
# ---------------
FROM jboss/base:latest

# Maintainer
# ----------
MAINTAINER Stefan Saupe <stefan.saupe@adcubum.com>


### Install Java
ADD java/jdk-7u80-linux-x64.tar.gz /opt/jboss
ENV JAVA_HOME /opt/jboss/jdk1.7.0_80

USER root
RUN rm -rf $JAVA_HOME/lib/visualvm && rm -rf $JAVA_HOME/lib/missioncontrol && rm -f $JAVA_HOME/src.zip
USER jboss

### Set Environment
ENV JBOSS_HOME /opt/jboss/jboss-eap-6.3

### Install EAP 6.3.0
ADD jboss/jboss-eap-6.3.0.zip /tmp/jboss-eap-6.3.0.zip
RUN unzip /tmp/jboss-eap-6.3.0.zip

### Add 6.3.3 patch
COPY jboss/jboss-eap-6.3.3-patch.zip /tmp/jboss-eap-6.3.3-patch.zip
RUN ${JBOSS_HOME}/bin/jboss-cli.sh --commands="patch apply /tmp/jboss-eap-6.3.3-patch.zip"


### Create EAP User
RUN $JBOSS_HOME/bin/add-user.sh admin welcome1! --silent

### Configure EAP
RUN echo "JAVA_OPTS=\"\$JAVA_OPTS -Djboss.bind.address=0.0.0.0 -Djboss.bind.address.management=0.0.0.0\"" >> $JBOSS_HOME/bin/standalone.conf

### Install dockerize for container dependencies
USER root
RUN yum -y install wget

ENV DOCKERIZE_VERSION v0.2.0
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz

USER jboss

### Open Ports
EXPOSE 8080 9990 9999

### Start EAP
CMD ["/opt/jboss/jboss-eap-6.3/bin/standalone.sh","-c","standalone-full.xml"]
