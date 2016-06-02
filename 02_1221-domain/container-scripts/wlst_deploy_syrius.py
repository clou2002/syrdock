JEE_ADM          = os.environ['JEE_ADM']
JEE_ADMPWD       = os.environ['JEE_ADMPWD']
JEE_ADM_HOSTNAME = os.environ['JEE_ADM_HOSTNAME']
JEE_ADM_PORT     = os.environ['JEE_ADM_PORT']

SYR_INSTANCE     = os.environ['SYR_INSTANCE']
JEE_HOME         = os.environ['JEE_HOME']
SYR_SECU_MODEL   = os.getenv('SYR_SECURITY_MODEL','DDOnly')

connect(JEE_ADM, JEE_ADMPWD, JEE_ADM_HOSTNAME + ':' + JEE_ADM_PORT)


# Check for Clusterenv
targetnames = ''
TARGET = getMBean('/Clusters/' + SYR_INSTANCE + '_clust')
if (TARGET == None):
  serverList = cmo.getServers();
  for server in serverList:
    if server.getName().startswith(SYR_INSTANCE):
      if targetnames:
        targetnames = targetnames + ','
      targetnames = targetnames + server.getName()
else:
  targetnames=TARGET.getName()


edit()
startEdit()
try:
  deploy(appName='syrius_services', path=JEE_HOME + '/ear/syrius_services.ear', targets=targetnames, securityModel=SYR_SECU_MODEL, timeout=3600000)
  save()
  activate()
  startApplication(appName='syrius_services')
except:
  #print >> sys.stderr, 'Error Deploy', SYR_INSTANCE
  #apply(traceback.print_exception, sys.exc_info())
  print 'ERROR RBS'
  print dumpStack()
