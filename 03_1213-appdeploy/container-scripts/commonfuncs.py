import os
import socket

# Variables
# =========
# Environment Vars
hostname       = socket.gethostname()
# Admin Vars
admin_username = os.environ.get('ADMIN_USERNAME', 'weblogic')
admin_password = os.environ.get('ADMIN_PASSWORD')
admin_host     = os.environ.get('ADMIN_HOST', 'wlsadmin')
admin_port     = os.environ.get('ADMIN_PORT', '8001')
# Node Manager Vars
nmname         = os.environ.get('NM_NAME', 'Machine-' + hostname)

# Functions
def editMode():
    edit()
    startEdit(waitTimeInMillis=-1, exclusive="false")

def saveActivate():
    save()
    activate(block="false")
	
def connectToAdmin():
    connect(admin_username, admin_password, 't3://' + admin_host + ':' + admin_port)
