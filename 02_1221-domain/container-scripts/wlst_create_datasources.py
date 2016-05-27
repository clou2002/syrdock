'''JEE_ADM          = os.environ['JEE_ADM']
JEE_ADMPWD       = os.environ['JEE_ADMPWD']
JEE_ADM_HOSTNAME = os.environ['JEE_ADM_HOSTNAME']
JEE_ADM_PORT     = os.environ['JEE_ADM_PORT']

SYR_INSTANCE = os.environ['SYR_INSTANCE']
DB_USER      = os.environ['DB_USER']
DB_USERPWD   = os.environ['DB_USERPWD']
DB_HOSTNAME  = os.environ['DB_HOSTNAME']
DB_SERVICE   = os.environ['DB_SERVICE']
DB_JDBC_URL  = os.environ['DB_JDBC_URL']
'''
import os
#import random
#import string
#import socket

execfile('commonfuncs.py')

domain_name  = os.environ.get("DOMAIN_NAME", "base_domain")
admin_port   = os.environ.get("ADMIN_PORT", "8001")
admin_pass   = os.environ.get("ADMIN_PASSWORD")
cluster_name = os.environ.get("CLUSTER_NAME", "DockerCluster")
domain_path  = '/u01/oracle/user_projects/domains/' + domain_name

DB_USER      = os.environ.get("DB_USER","SYRIUS")
DB_USERPWD   = os.environ.get("DB_USERPWD","cube12")
#Hostname 'docker' wird der machine mit --add-host mitgegeben und in die /etc/hosts eingetragen
DB_JDBC_URL  = os.environ.get("DB_JDBC_URL","jdbc:oracle:thin:@//docker:1521/orcl")


# Connect to the AdminServer
# ==========================
connectToAdmin()

# Create blablah
# ======================
editMode()

TARGET = getMBean('/Clusters/' + cluster_name)
cd('/')

# Step 3 - up to deployment - setting the DB-conn

jdbc_ds_0='SyriusDS'

create(jdbc_ds_0, 'JDBCSystemResources')
cd('/JDBCSystemResources/'+jdbc_ds_0+'/JDBCResource/'+jdbc_ds_0+'/JDBCConnectionPoolParams/'+jdbc_ds_0)
cmo.setMaxCapacity(30)
cmo.setStatementTimeout(60)
set('TestConnectionsOnReserve', 'true')
set('TestTableName', 'SQL SELECT 1 FROM DUAL')
cd('/JDBCSystemResources/'+jdbc_ds_0+'/JDBCResource/'+jdbc_ds_0)
set('Name', jdbc_ds_0)

cd('/JDBCSystemResources/'+jdbc_ds_0+'/JDBCResource/'+jdbc_ds_0+'/JDBCDriverParams/'+jdbc_ds_0)
set('Password', DB_USERPWD)
set('Url', DB_JDBC_URL)
set('DriverName', 'oracle.jdbc.xa.client.OracleXADataSource')

cd('/JDBCSystemResources/'+jdbc_ds_0+'/JDBCResource/'+jdbc_ds_0+'/JDBCDataSourceParams/'+jdbc_ds_0)
cmo.setGlobalTransactionsProtocol('TwoPhaseCommit')
set('JNDINames', jarray.array(["jdbc/SyriusDS"], String))

cd('/JDBCSystemResources/'+jdbc_ds_0+'/JDBCResource/'+jdbc_ds_0+'/JDBCDriverParams/'+jdbc_ds_0+'/Properties/'+jdbc_ds_0)
cmo.createProperty('user')
cd('/JDBCSystemResources/'+jdbc_ds_0+'/JDBCResource/'+jdbc_ds_0+'/JDBCDriverParams/'+jdbc_ds_0+'/Properties/'+jdbc_ds_0+'/Properties/user')
set('Value', DB_USER)
set('Name', 'user')

cd('/JDBCSystemResources/'+jdbc_ds_0+'/JDBCResource/'+jdbc_ds_0+'/JDBCXAParams/'+jdbc_ds_0)
set('XaTransactionTimeout','10800')
set('XaSetTransactionTimeout','true')

cd('/JDBCSystemResources/'+jdbc_ds_0)
cmo.addTarget(TARGET)


jdbc_ds_1='SyriusNewTransactionDS'

cd('/')
create(jdbc_ds_1, 'JDBCSystemResources')
cd('/JDBCSystemResources/'+jdbc_ds_1+'/JDBCResource/'+jdbc_ds_1+'/JDBCConnectionPoolParams/'+jdbc_ds_1)
cmo.setStatementTimeout(60)
set('TestConnectionsOnReserve', 'true')
set('TestTableName', 'SQL SELECT 1 FROM DUAL')
cd('/JDBCSystemResources/'+jdbc_ds_1+'/JDBCResource/'+jdbc_ds_1)
set('Name', jdbc_ds_1)

cd('/JDBCSystemResources/'+jdbc_ds_1+'/JDBCResource/'+jdbc_ds_1+'/JDBCDriverParams/'+jdbc_ds_1)
set('Password', DB_USERPWD)
set('Url', DB_JDBC_URL)
set('DriverName', 'oracle.jdbc.driver.OracleDriver')

cd('/JDBCSystemResources/'+jdbc_ds_1+'/JDBCResource/'+jdbc_ds_1+'/JDBCDataSourceParams/'+jdbc_ds_1)
cmo.setGlobalTransactionsProtocol('OnePhaseCommit')
set('JNDINames', jarray.array(['jdbc/SyriusNewTransactionDS'], String))

cd('/JDBCSystemResources/'+jdbc_ds_1+'/JDBCResource/'+jdbc_ds_1+'/JDBCDriverParams/'+jdbc_ds_1+'/Properties/'+jdbc_ds_1)
cmo.createProperty('user')
cd('/JDBCSystemResources/'+jdbc_ds_1+'/JDBCResource/'+jdbc_ds_1+'/JDBCDriverParams/'+jdbc_ds_1+'/Properties/'+jdbc_ds_1+'/Properties/user')
set('Value', DB_USER)
set('Name', 'user')

cd('/JDBCSystemResources/'+jdbc_ds_1)
cmo.addTarget(TARGET)


jdbc_ds_2='SyriusBatchDS'

cd('/')
create(jdbc_ds_2, 'JDBCSystemResources')
cd('/JDBCSystemResources/'+jdbc_ds_2+'/JDBCResource/'+jdbc_ds_2+'/JDBCConnectionPoolParams/'+jdbc_ds_2)
cmo.setMaxCapacity(30)
cmo.setStatementTimeout(10800)
set('TestConnectionsOnReserve', 'true')
set('TestTableName', 'SQL SELECT 1 FROM DUAL')
cd('/JDBCSystemResources/'+jdbc_ds_2+'/JDBCResource/'+jdbc_ds_2)
set('Name', jdbc_ds_2)

cd('/JDBCSystemResources/'+jdbc_ds_2+'/JDBCResource/'+jdbc_ds_2+'/JDBCDriverParams/'+jdbc_ds_2)
set('Password', DB_USERPWD)
set('Url', DB_JDBC_URL)
set('DriverName', 'oracle.jdbc.xa.client.OracleXADataSource')

cd('/JDBCSystemResources/'+jdbc_ds_2+'/JDBCResource/'+jdbc_ds_2+'/JDBCDataSourceParams/'+jdbc_ds_2)
cmo.setGlobalTransactionsProtocol('TwoPhaseCommit')
set('JNDINames', jarray.array(["jdbc/SyriusBatchDS"], String))

cd('/JDBCSystemResources/'+jdbc_ds_2+'/JDBCResource/'+jdbc_ds_2+'/JDBCDriverParams/'+jdbc_ds_2+'/Properties/'+jdbc_ds_2)
cmo.createProperty('user')
cd('/JDBCSystemResources/'+jdbc_ds_2+'/JDBCResource/'+jdbc_ds_2+'/JDBCDriverParams/'+jdbc_ds_2+'/Properties/'+jdbc_ds_2+'/Properties/user')
set('Value', DB_USER)
set('Name', 'user')

cd('/JDBCSystemResources/'+jdbc_ds_2+'/JDBCResource/'+jdbc_ds_2+'/JDBCXAParams/'+jdbc_ds_2)
set('XaTransactionTimeout','10800')
set('XaSetTransactionTimeout','true')

cd('/JDBCSystemResources/'+jdbc_ds_2)
cmo.addTarget(TARGET)


jdbc_ds_4='SyriusMonitoringDS'

cd('/')
create(jdbc_ds_4, 'JDBCSystemResources')
cd('/JDBCSystemResources/'+jdbc_ds_4+'/JDBCResource/'+jdbc_ds_4+'/JDBCConnectionPoolParams/'+jdbc_ds_4)
cmo.setMaxCapacity(30)
cmo.setTestTableName('SQL SELECT 1 FROM DUAL')
cmo.setTestConnectionsOnReserve(true)
cmo.setStatementTimeout(60)

cd('/JDBCSystemResources/'+jdbc_ds_4+'/JDBCResource/'+jdbc_ds_4)
cmo.setName(jdbc_ds_4)

cd('/JDBCSystemResources/'+jdbc_ds_4+'/JDBCResource/'+jdbc_ds_4+'/JDBCDriverParams/'+jdbc_ds_4)
cmo.setUrl(DB_JDBC_URL)
cmo.setDriverName('oracle.jdbc.xa.client.OracleXADataSource')
cmo.setPassword(DB_USERPWD)

cd('/JDBCSystemResources/'+jdbc_ds_4+'/JDBCResource/'+jdbc_ds_4+'/JDBCDataSourceParams/'+jdbc_ds_4)
cmo.setGlobalTransactionsProtocol('TwoPhaseCommit')
set('JNDINames', jarray.array(["jdbc/SyriusMonitoringDS"], String))

cd('/JDBCSystemResources/'+jdbc_ds_4+'/JDBCResource/'+jdbc_ds_4+'/JDBCDriverParams/'+jdbc_ds_4+'/Properties/'+jdbc_ds_4)
cmo.createProperty('user')
cd('/JDBCSystemResources/'+jdbc_ds_4+'/JDBCResource/'+jdbc_ds_4+'/JDBCDriverParams/'+jdbc_ds_4+'/Properties/'+jdbc_ds_4+'/Properties/user')
set('Value', DB_USER)
set('Name', 'user')

cd('/JDBCSystemResources/'+jdbc_ds_4+'/JDBCResource/'+jdbc_ds_4+'/JDBCXAParams/'+jdbc_ds_4)
cmo.setXaTransactionTimeout(7200)
cmo.setXaSetTransactionTimeout(true)

cd('/JDBCSystemResources/'+jdbc_ds_4)
cmo.addTarget(TARGET)


saveActivate()
exit()
