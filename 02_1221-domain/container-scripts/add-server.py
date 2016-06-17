# Copyright (c) 2014-2016 Oracle and/or its affiliates. All rights reserved.
#
# Script to create and add a Managed Server automatically to the domain's AdminServer running on 'wlsadmin'.
#
# Since: October, 2014
# Author: bruno.borges@oracle.com
#
# =============================
import os
import random
import string
import socket

execfile('commonfuncs.py')

# Functions
def randomName():
  return ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(6)])

# AdminServer details
cluster_name = os.environ.get("CLUSTER_NAME", "DockerCluster")

# ManagedServer details
msinternal = socket.gethostbyname(hostname)
msname = os.environ.get('MS_NAME', 'ManagedServer-' + randomName() + '@' + hostname)
mshost = os.environ.get('MS_HOST', msinternal)
msport = os.environ.get('MS_PORT', '7001')
memargs = os.environ.get('USER_MEM_ARGS', '')

# Connect to the AdminServer
# ==========================
connectToAdmin()

# Create a ManagedServer
# ======================
editMode()
cd('/')
cmo.createServer(msname)

cd('/Servers/' + msname)
cmo.setMachine(getMBean('/Machines/' + nmname))
cmo.setCluster(getMBean('/Clusters/' + cluster_name))

# Default Channel for ManagedServer
# ---------------------------------
cmo.setListenAddress(msinternal)
cmo.setListenPort(int(msport))
cmo.setListenPortEnabled(true)
cmo.setExternalDNSName(mshost)

# Disable SSL for this ManagedServer
# ----------------------------------
cd('/Servers/' + msname + '/SSL/' + msname)
cmo.setEnabled(false)

# Custom Channel for ManagedServer
# --------------------------------
#cd('/Servers/' + msname)
#cmo.createNetworkAccessPoint('Channel-0')

#cd('/Servers/' + msname + '/NetworkAccessPoints/Channel-0')
#cmo.setProtocol('t3')
#cmo.setEnabled(true)
#cmo.setPublicAddress(mshost)
#cmo.setPublicPort(int(msport))
#cmo.setListenAddress(msinternal)
#cmo.setListenPort(int(msport))
#cmo.setHttpEnabledForThisProtocol(true)
#cmo.setTunnelingEnabled(false)
#cmo.setOutboundEnabled(false)
#cmo.setTwoWaySSLEnabled(false)
#cmo.setClientCertificateEnforced(false)

# Custom Startup Parameters because NodeManager writes wrong AdminURL in startup.properties
# -----------------------------------------------------------------------------------------
cd('/Servers/' + msname + '/ServerStart/' + msname)
arguments = '-Djava.security.egd=file:/dev/./urandom -Dweblogic.Name=' + msname + ' -Dweblogic.management.server=http://' + admin_host + ':' + admin_port + ' ' + memargs
arguments = arguments + ' -Xmx3000M -Dsyrius.log4j.configuration.watch_interval=5000 \
                          -Dsyrius.log4j.configuration.reconfigure=true \
						  -Dsyrius.profiling=true \
						  -Dsyrius.WebserviceEndpointConfig=file:///u01/oracle/syrius/config/jee_EndpointConfig.xml \
						  -Dcom.sun.xml.namespace.QName.useCompatibleSerialVersionUID=1.0 \
						  -Dsyrius.default_userid=SyriusAdmin \
						  -Dsyrius.urldef.placeholder.conf=/u01/oracle/syrius/config/syrius.urldef.conf \
						  -XX:+UnlockCommercialFeatures \
						  -XX:+FlightRecorder  \
						  -Dsyrius.searchengine_clustername=syriusEsCluster_HEAD_HANGAR_A \
						  -Dsyrius.searchengine_tcptransportport=23417 \
						  -Dlogstreamer.profiles=/u01/oracle/LogStreamerProfiles.xml \
						  -Dlogstreamer.jgroups_config=file:///u01/oracle/syrius/config/fl_jgroups.xml \
						  -Dlogstreamer.jgroups_name=HEAD_HANGAR_A \
						  -Dlogstreamer.name=HEAD_HANGAR_A_test \
						  -Xdebug -Xnoagent -Xrunjdwp:transport=dt_socket,address=23411,server=y,suspend=n \
						  -Dhttps.proxySet=true \
						  -Dhttps.proxyHost=172.21.131.12 \
						  -Dhttps.proxyPort=8080 \
						  -Dsyrius.ldap.config=file:////u01/oracle/syrius/config/activeDirectory.conf \
						  -Djava.security.auth.login.config=/u01/oracle/syruser-auth-AD.conf \
						  -Dsyrius.default_userid=SyriusAdmin \
						  -XX:+UseCompressedOops \
						  -Duser.language=de \
						  -Duser.region=CH \
						  -Duser.timezone=Europe/Zurich \
						  -Djava.net.preferIPv4Stack=true \
						  -Dsyrius.log4j.reconfigure=true -Djava.util.Arrays.useLegacyMergeSort=true \
						  -Dsun.lang.ClassLoader.allowArraySyntax=true \
						  -Dsyrius.jta.TransactionManagerName=javax.transaction.TransactionManager \
						  -Dsyrius.help.useprocessdef=true \
						  -Dsyrius.auditlogger=/u01/oracle/syrius/config/auditlog.xml \
						  -Dlog4j.configuration=/u01/oracle/syrius/config/jee_log4j.xml \
						  -Dsyrius.cache.jgroups.config=file:/u01/oracle/syrius/config/jee_jgroups_conf.xml \
						  -Ddb_type=oracle'
cmo.setArguments(arguments)
saveActivate()

# Start Managed Server
# ------------
try:
    start(msname, 'Server')
except:
    dumpStack()

# Exit
# =========
exit()
