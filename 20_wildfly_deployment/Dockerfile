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
#      $ docker build -t clou/syr:3_06_HEAD .
#

# Pull base image
# ---------------
FROM jboss/wildfly:9.0.2.Final

# Maintainer
# ----------
MAINTAINER Stefan Saupe <stefan.saupe@adcubum.com>

# Define variables
#ARG ADMIN_PASSWORD
ENV JAVA_OPTS="-Xmx3000M -XX:MaxPermSize=1024M -Dsyrius.log4j.configuration.watch_interval=5000 -Dsyrius.log4j.configuration.reconfigure=true -Dsyrius.profiling=true -Dsyrius.WebserviceEndpointConfig=file:///opt/jboss/syrius/config/jee_EndpointConfig.xml -XX:MaxPermSize=1024M -Djava.net.preferIPv4Stack=true -Dorg.jboss.as.logging.per-deployment=false -Dlog4j.configuration=/opt/jboss/syrius/config/jee_log4j.xml -Dsyrius.searchengine_configfile=/opt/jboss/syrius/config/es_config.yml -Dlogstreamer.profiles=/opt/jboss/syrius/config/LogStreamerProfiles.xml -Dlogstreamer.jgroups_config=file:///opt/jboss/syrius/config/fl_jgroups.xml -Dlogstreamer.jgroups_name=GENERALI_O -Dlogstreamer.name=GENERALI_O_test -Xdebug -Xnoagent -Xrunjdwp:transport=dt_socket,address=42711,server=y,suspend=n -Djava.security.auth.login.config=/opt/jboss/syrius/config/jee_auth.conf -Dsyrius.default_userid=admin“


RUN mkdir syrius
RUN mkdir syrius/logs

# Copy files and deploy application
COPY syrius/bin syrius/bin
COPY syrius/config syrius/config

COPY syrius/config/standalone-full-syrius.xml /opt/jboss/wildfly/standalone/configuration/
ADD syrius/software/syrius_services.ear /opt/jboss/wildfly/standalone/deployments/


#CMD ["/opt/jboss/wildfly/bin/standalone.sh -c standalone-full-syrius.xml -P /opt/jboss/syrius/config/jboss.config > /opt/jboss/syrius/logs/jboss.log 2>&1 &"]
CMD ["/opt/jboss/wildfly/bin/standalone.sh","-c","standalone-full-syrius.xml","-P","/opt/jboss/syrius/config/jboss.config"]