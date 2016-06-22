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
FROM clou/syr:jboss-eap-6

# Maintainer
# ----------
MAINTAINER Stefan Saupe <stefan.saupe@adcubum.com>

# Define variables
#ARG ADMIN_PASSWORD
ENV JAVA_OPTS="-Xmx3000M -XX:MaxPermSize=1024M -Dsyrius.log4j.configuration.watch_interval=5000 -Dsyrius.log4j.configuration.reconfigure=true -Dsyrius.profiling=true -Dsyrius.WebserviceEndpointConfig=file:///opt/jboss/syrius/config/jee_EndpointConfig.xml -XX:MaxPermSize=1024M -Djava.net.preferIPv4Stack=true -Dorg.jboss.as.logging.per-deployment=false -Dlog4j.configuration=/opt/jboss/syrius/config/jee_log4j.xml -Dsyrius.searchengine_configfile=/opt/jboss/syrius/config/es_config.yml -Dlogstreamer.profiles=/opt/jboss/syrius/config/LogStreamerProfiles.xml -Dlogstreamer.jgroups_config=file:///opt/jboss/syrius/config/fl_jgroups.xml -Dlogstreamer.jgroups_name=GENERALI_O -Dlogstreamer.name=GENERALI_O_test -Xdebug -Xnoagent -Xrunjdwp:transport=dt_socket,address=42711,server=y,suspend=n -Djava.security.auth.login.config=/opt/jboss/syrius/config/jee_auth.conf -Dsyrius.default_userid=admin“

ENV UTC_HOME=/opt/jboss/syrius/ASE-UTC-Server
ENV UTC_JVM_ARGS="-Xmx1000M -XX:MaxPermSize=256M -Dsyrius.profiling=true -Djavax.xml.bind.JAXBContext=com.sun.xml.bind.v2.ContextFactory -Dsyrius.auditlogger=/opt/jboss/syrius/config/auditlog.xml -Dsyrius.adcubum_intern=true -Dlogstreamer.profiles=//opt/jboss/syrius/config/LogStreamerProfiles.xml -Dlogstreamer.jgroups_config=file:///opt/jboss/syrius/config/fl_jgroups.xml -Dlogstreamer.jgroups_name=GENERALI_O -Dlogstreamer.name=GENERALI_O_test"
ENV UTC_PORT=8081
ENV SYRMAN_LOG=/opt/jboss/syrius/logs
ENV SYRMAN_CFG=/opt/jboss/syrius/config

RUN mkdir syrius
RUN mkdir syrius/logs

# Copy files and deploy application
COPY jboss/modules $JBOSS_HOME/modules
COPY syrius/bin syrius/bin
COPY syrius/config syrius/config

COPY syrius/config/standalone-full-syrius.xml $JBOSS_HOME/standalone/configuration/
COPY syrius/software/rel3_06_HEAD_generali_auslieferung/Executables/ASE-J2EE-Server/ear/syrius_services.ear $JBOSS_HOME/standalone/deployments/
COPY syrius/software/rel3_06_HEAD_generali_auslieferung/Executables/ASE-UTC-Server/ syrius/ASE-UTC-Server/

USER root
RUN chown -R jboss:jboss /opt/jboss/syrius
USER jboss

EXPOSE 8080 9990 9999 $UTC_PORT

CMD ["/opt/jboss/jboss-eap-6.3/bin/standalone.sh","-c","standalone-full-syrius.xml","-P","/opt/jboss/syrius/config/jboss.config"]