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
#      $ docker build -t 1213-appdeploy .
#

# Pull base image
# ---------------
FROM clou/wls:12.1.3-domain

# Maintainer
# ----------
MAINTAINER Stefan Saupe <stefan.saupe@adcubum.com>

# Define variables
#ARG ADMIN_PASSWORD
ENV ADMIN_PASSWORD="$ADMIN_PASSWORD" \
    ADMIN_PORT="8001" \
    ADMIN_HOST="wlsadmin" \
    APP_NAME="syrius_services" \
    APP_PKG_FILE="syrius_services.ear" \
    APP_PKG_LOCATION="/u01/oracle"

# Copy files and deploy application in WLST Offline mode
COPY container-scripts/*.py /u01/oracle/
COPY container-scripts/*.ear /u01/oracle/


RUN wlst.sh /u01/oracle/app-deploy_online.py
