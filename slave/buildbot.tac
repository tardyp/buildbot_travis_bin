import os
import sys
import json

from twisted.application import service
from buildslave.wamp import WampBuildSlave
from twisted.application import strports
from twisted.web import server
from twisted.web.static import File

# setup slave
basedir = os.path.abspath(os.path.dirname(__file__))

os.system("cp -r .ssh .. && chmod -R 700 ../.ssh")
os.system("ssh-keyscan  -t rsa,dsa -p 29418 android.intel.com > ../.ssh/known_hosts")
os.system("ssh sys_bbmain@android.intel.com -p 29418")

# Default umask for server
umask = None

# note: this line is matched against to check that this is a buildslave
# directory; do not edit it.
application = service.Application('buildslave')
import sys
num_slaves = int(os.environ("NUM_SLAVES", 1))
from twisted.python.log import ILogObserver, FileLogObserver

application.setComponent(ILogObserver, FileLogObserver(sys.stdout).emit)

for i in xrange(num_slaves):
    slavename = "slave%d" % (i,)
    m = BuildSlave("localhost", 19989, "buildbot", slavename , "pass", os.path.join(basedir, slavename), False)
    m.setServiceParent(application)
