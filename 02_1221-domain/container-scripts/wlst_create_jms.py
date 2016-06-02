'''JEE_ADM          = os.environ['JEE_ADM']
JEE_ADMPWD       = os.environ['JEE_ADMPWD']
JEE_ADM_HOSTNAME = os.environ['JEE_ADM_HOSTNAME']


SYR_INSTANCE = os.environ['SYR_INSTANCE']
DB_USER      = os.environ['DB_USER']
DB_USERPWD   = os.environ['DB_USERPWD']
DB_HOSTNAME  = os.environ['DB_HOSTNAME']
DB_SERVICE   = os.environ['DB_SERVICE']
DB_JDBC_URL  = os.environ['DB_JDBC_URL']
'''
import os
import random
import string
import socket

execfile('commonfuncs.py')

domain_name  = os.environ.get("DOMAIN_NAME", "base_domain")
admin_port   = os.environ.get("ADMIN_PORT", "8001")
admin_pass   = os.environ.get("ADMIN_PASSWORD")
cluster_name = os.environ.get("CLUSTER_NAME", "DockerCluster")
domain_path  = '/u01/oracle/user_projects/domains/' + domain_name

DB_USER      = os.environ.get("DB_USER","SYRIUS")
DB_USERPWD   = os.environ.get("DB_USERPWD","cube12")
DB_JDBC_URL  = os.environ.get("DB_JDBC_URL","jdbc:oracle:thin:@//docker:1521/orcl")

# Connect to the AdminServer
# ==========================
connectToAdmin()

# Create blablah
# ======================
editMode()
print '###wlst_create_jms.py Step 1'
TARGET = getMBean('/Clusters/' + cluster_name)
cd('/')
print '###wlst_create_jms.py Step 2'
jms_module='SyriusAQJMSModule'

try:
  print '###wlst_create_jms.py Step 3'
  cd('/JMSSystemResources/'+jms_module)
  print '===> JMS datasource '+jms_module+' already exists'
except:
  print '###wlst_create_jms.py Step 4'
  print '===> Creating JMS datasource '+jms_module
  cd('/')
  cmo.createJMSSystemResource(jms_module)

  cd('/JMSSystemResources/'+jms_module)
  cmo.addTarget(TARGET)
  #set('Targets',jarray.array([ObjectName('com.bea:Name=XXX_clust,Type=Cluster')], ObjectName))

  cd('/JMSSystemResources/'+jms_module+'/JMSResource/'+jms_module)
  cmo.createForeignServer('SyriusJMSForeignServer')

  cd('/JMSSystemResources/'+jms_module+'/JMSResource/'+jms_module+'/ForeignServers/SyriusJMSForeignServer')
  cmo.setDefaultTargetingEnabled(true)
  cmo.setInitialContextFactory('oracle.jms.AQjmsInitialContextFactory')
  cmo.unSet('JNDIPropertiesCredentialEncrypted')
  cmo.createJNDIProperty('datasource')

  cd('/JMSSystemResources/'+jms_module+'/JMSResource/'+jms_module+'/ForeignServers/SyriusJMSForeignServer/JNDIProperties/datasource')
  cmo.setValue('jdbc/SyriusMessagesDS')



  cd('/JMSSystemResources/'+jms_module+'/JMSResource/'+jms_module+'/ForeignServers/SyriusJMSForeignServer')
  cmo.createForeignDestination('SyriusEventQueueData')

  cd('/JMSSystemResources/'+jms_module+'/JMSResource/'+jms_module+'/ForeignServers/SyriusJMSForeignServer/ForeignDestinations/SyriusEventQueueData')
  cmo.setLocalJNDIName('jms/SyriusEventQueueData')
  cmo.setRemoteJNDIName('Queues/SYR_Q_DATA')


  cd('/JMSSystemResources/'+jms_module+'/JMSResource/'+jms_module+'/ForeignServers/SyriusJMSForeignServer')
  cmo.createForeignDestination('SyriusEventQueueError')

  cd('/JMSSystemResources/'+jms_module+'/JMSResource/'+jms_module+'/ForeignServers/SyriusJMSForeignServer/ForeignDestinations/SyriusEventQueueError')
  cmo.setLocalJNDIName('jms/SyriusEventQueueError')
  cmo.setRemoteJNDIName('Queues/AQ$_SYR_QT_DATA_E')



  cd('/JMSSystemResources/'+jms_module+'/JMSResource/'+jms_module+'/ForeignServers/SyriusJMSForeignServer')
  cmo.createForeignConnectionFactory('SyriusQueueConnectionFactory')

  cd('/JMSSystemResources/'+jms_module+'/JMSResource/'+jms_module+'/ForeignServers/SyriusJMSForeignServer/ForeignConnectionFactories/SyriusQueueConnectionFactory')
  cmo.setLocalJNDIName('jms/SyriusQueueConnectionFactory')
  cmo.setRemoteJNDIName('XAQueueConnectionFactory')


  cd('/')
  jms_ds='SyriusMessagesDS'
  cmo.createJDBCSystemResource(jms_ds)

  cd('/JDBCSystemResources/'+jms_ds+'/JDBCResource/'+jms_ds)
  cmo.setName(jms_ds)

  cd('/JDBCSystemResources/'+jms_ds+'/JDBCResource/'+jms_ds+'/JDBCDataSourceParams/'+jms_ds)
  set('JNDINames',jarray.array([String('jdbc/SyriusMessagesDS')], String))

  cd('/JDBCSystemResources/'+jms_ds+'/JDBCResource/'+jms_ds+'/JDBCDriverParams/'+jms_ds)
  cmo.setUrl(DB_JDBC_URL)
  cmo.setDriverName('oracle.jdbc.xa.client.OracleXADataSource')
  cmo.setPassword(DB_USERPWD)

  cd('/JDBCSystemResources/'+jms_ds+'/JDBCResource/'+jms_ds+'/JDBCConnectionPoolParams/'+jms_ds)
  cmo.setTestTableName('SQL SELECT 1 FROM DUAL')

  cd('/JDBCSystemResources/'+jms_ds+'/JDBCResource/'+jms_ds+'/JDBCDriverParams/'+jms_ds+'/Properties/'+jms_ds)
  cmo.createProperty('user')

  cd('/JDBCSystemResources/'+jms_ds+'/JDBCResource/'+jms_ds+'/JDBCDriverParams/'+jms_ds+'/Properties/'+jms_ds+'/Properties/user')
  cmo.setValue(DB_USER)

  cd('/JDBCSystemResources/'+jms_ds+'/JDBCResource/'+jms_ds+'/JDBCDataSourceParams/'+jms_ds)
  cmo.setGlobalTransactionsProtocol('TwoPhaseCommit')

  cd('/JDBCSystemResources/'+jms_ds+'/JDBCResource/'+jms_ds+'/JDBCXAParams/'+jms_ds)
  cmo.setXaTransactionTimeout(10800)
  cmo.setXaSetTransactionTimeout(true)

  cd('/JDBCSystemResources/'+jms_ds)
  cmo.addTarget(TARGET)
  #set('Targets',jarray.array([ObjectName('com.bea:Name=' + SYR_INSTANCE + ',Type=Server')], ObjectName))

  

saveActivate()
exit()