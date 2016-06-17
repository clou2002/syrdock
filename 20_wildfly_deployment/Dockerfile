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
FROM jboss/wildfly

# Maintainer
# ----------
MAINTAINER Stefan Saupe <stefan.saupe@adcubum.com>

# Define variables
#ARG ADMIN_PASSWORD


# Copy files and deploy application
ADD syrius/software/syrius_services.ear /opt/jboss/wildfly/standalone/deployments/
