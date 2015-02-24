import os
import json

from twisted.application import service
from buildbot.master import BuildMaster

appconfig = json.loads(os.environ.get('VCAP_APPLICATION', '{}'))

old_uname = os.uname

os.system("cp -r .ssh .. && chmod -R 700 ../.ssh")
os.system("ssh-keyscan  -t rsa,dsa -p 29418 android.intel.com > ../.ssh/known_hosts")
os.system("ssh sys_bbmain@android.intel.com -p 29418")

def uname():
    ret = list(old_uname())
    ret[1] = "%s%d" % (appconfig.get('application_name', "bbtravis"), appconfig.get('instance_index', 0))
    return tuple(ret)
os.uname = uname
print os.uname()
# setup master
basedir = os.path.abspath(os.path.dirname(__file__))
configfile = 'config.py'

# Default umask for server
umask = None

# note: this line is matched against to check that this is a buildmaster
# directory; do not edit it.
application = service.Application('buildmaster')
import sys

from twisted.python.log import ILogObserver, FileLogObserver

application.setComponent(ILogObserver, FileLogObserver(sys.stdout).emit)

m = BuildMaster(basedir, configfile, umask)
m.setServiceParent(application)
