# LICENSE CDDL 1.0 + GPL 2.0
#
# Copyright (c) 2015 Oracle and/or its affiliates. All rights reserved.
# 
# ORACLE DOCKERFILES PROJECT
# --------------------------
# This Dockerfile extends the Oracle WebLogic image built under 1221-domain with tag name '1221-domain'
#
# It will deploy any package defined in APP_PKG_FILE located in APP_PKG_LOCATION
# into the DOMAIN_HOME with name defined in APP_NAME
#
# HOW TO BUILD THIS IMAGE
# -----------------------
# Run: 
#      $ docker build -t clou/syr:eap6jdk7 .
#

# Pull base image
# ---------------
FROM jboss/base-jdk:7

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

### Open Ports
EXPOSE 8080 9990 9999

### Start EAP
CMD ["/opt/jboss/jboss-eap-6.3/bin/standalone.sh","-c","standalone-full.xml"]
