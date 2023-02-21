from fabric.api import *

# Set the name of the user login to the remote host

env.user = 'student'
env.port = '8347'
env.hosts =['myvmlab.senecacollege.ca']


# Define the task to get the hostname of remote machines:
def getHostname():
    name = run("hostname")
    print("The host name is:",name)

def installPackage(pkg='dummy'):
    cmd = 'yum install ' + pkg + ' -y'
    status = sudo(cmd)
    print(status)

def removePackage(pkg=''):
    if pkg == '':
       cmd = 'yum remove dummy -y'
    else:
       cmd = 'yum remove ' + pkg + ' -y'
    status = sudo(cmd)
    print(status)

def updatePackage(pkg=''):
    if pkg == '':
        cmd = 'yum update ' + pkg + ' -y'
    else:
        cmd = 'yum update -y --skip-broken'
    status = sudo(cmd)
    print(status)


def makeUser():
    if usr == '':
        cmd = 'useradd ' + usr + ' -m'
        print('User' + usr + 'created') 

def makeUser():
    sudo("useradd -m -d /home/ops445p ops445p")
    sudo("usermod -a -G wheel ops445p")
    sudo("mkdir ~ops445p/.ssh/")
    sudo("chmod 700 ~ops445p/.ssh")
    sudo("touch ~ops445p/.ssh/authorized_keys")
    sudo("chmod 600 ~ops445p/.ssh/authorized_keys")
    sudo("ssh nnimalan@matrix.senecacollege.ca 'cat ~ahad.mammadov/ops445p.pub' >>  ~ops445p/.ssh/authorized_keys")
    print("User ops445p created")
    print("User ops445p added to wheel group")
    print("Created .ssh directory in ops445p home directory")
    print("Changed permissions for ~ops445p/.ssh directory")
    print("Created authorized_keys files under ~ops445p/.ssh/")
    print("Changed permissions for authorized_keys file.")
    print("Added ops445p.pub key to authorized_keys.")
