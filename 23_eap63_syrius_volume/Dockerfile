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
#      $ docker build -t clou/syr:3_06_HEAD_vol .
#

# Pull base image
# ---------------
FROM clou/syr:eap6jdk7

# Maintainer
# ----------
MAINTAINER Stefan Saupe <stefan.saupe@adcubum.com>

# Define variables

ENV UTC_PORT=42703
ENV DB_USER=syriusdocker
ENV DB_USERPWD=cube12
ENV DB_JDBC_URL=jdbc:oracle:thin:@(DESCRIPTION=(ADDRESS_LIST=(ADDRESS=(PROTOCOL=TCP)(HOST=192.168.99.1)(PORT=1521)))(CONNECT_DATA=(SERVICE_NAME=orcl)(SERVER=DEDICATED)))

ENV SYRMAN_LOG=/opt/jboss/syrius/logs
ENV SYRMAN_CFG=/opt/jboss/syrius/config
ENV SYR_INSTANCE_ROOT=/opt/jboss/syrius

RUN mkdir syrius
RUN mkdir syrius/logs

# Copy files and deploy application
#COPY syrius/properties syrius/properties
#COPY syrius/bin syrius/bin
#COPY syrius/config syrius/config

#COPY syrius/config/standalone-full-syrius.xml $JBOSS_HOME/standalone/configuration/
#COPY syrius/software/Executables/ASE-J2EE-Server/ear/syrius_services.ear $JBOSS_HOME/standalone/deployments/
#COPY syrius/software/Executables/ASE-UTC-Server/ syrius/ASE-UTC-Server/

USER root
RUN chown -R jboss:jboss /opt/jboss/syrius
USER jboss

EXPOSE 42705 42707  9990 9999 $UTC_PORT

CMD ["/opt/jboss/syrius/bin/jboss_start"]