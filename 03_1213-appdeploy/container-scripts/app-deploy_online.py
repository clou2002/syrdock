# Copyright (c) 2014-2016 Oracle and/or its affiliates. All rights reserved.
#
# Script to create and add NodeManager automatically to the domain's AdminServer running on '$ADMIN_HOST'.
#
# Since: October, 2014
# Author: stefan.saupe@adcubum.com
#
# =============================
import os

# Deployment Information 

domainhome = os.environ.get('DOMAIN_HOME', '/u01/oracle/user_projects/domains/base_domain')
appname    = os.environ.get('APP_NAME', 'sample')
apppkg     = os.environ.get('APP_PKG_FILE', 'sample.war')
appdir     = os.environ.get('APP_PKG_LOCATION', '/u01/oracle')
cluster_name = os.environ.get("CLUSTER_NAME", "DockerCluster")

execfile('commonfuncs.py')

# Connect to the AdminServer
# ==========================
connectToAdmin()

# Deploy the stuff
# ================
editMode()

try:
  deploy(appName=appname, path=appdir + '/' + apppkg, targets=cluster_name, securityModel='DDOnly', timeout=3600000)
  saveActivate()
  startApplication(appName=appname)
except:
  printdumpStack()
# Exit
# ====
exit()
