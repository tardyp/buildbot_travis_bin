import os
import sys
import json

from twisted.application import service
from buildslave.bot import BuildSlave
from twisted.application import strports
from twisted.web import server
from twisted.web.static import File

# setup slave
basedir = os.path.abspath(os.path.dirname(__file__))

# Default umask for server
umask = None

# note: this line is matched against to check that this is a buildslave
# directory; do not edit it.
application = service.Application('buildslave')
import sys
num_slaves = int(os.environ.get("NUM_SLAVES", 1))
from twisted.python.log import ILogObserver, FileLogObserver

application.setComponent(ILogObserver, FileLogObserver(sys.stdout).emit)
keepalive = 600
usepty = 0
umask = None
maxdelay = 300
allow_shutdown = None

for i in xrange(num_slaves):
    slavename = "slave%d" % (i,)
    slavedir = os.path.join(basedir, slavename)
    os.system("mkdir -p " + slavedir)
    s = BuildSlave("localhost", 19989, slavename , "pass", slavedir,
                   keepalive, usepty, umask=umask, maxdelay=maxdelay,
                   allow_shutdown=allow_shutdown)
    s.setServiceParent(application)
