import os
import sys

from twisted.application import service
from twisted.python.log import ILogObserver, FileLogObserver
from buildbot.master import BuildMaster

# setup master
basedir = os.path.abspath(os.path.dirname(__file__))
configfile = os.path.join(basedir, 'config.py')
basedir = os.path.join(basedir, 'workdir')
os.system("mkdir -p " + basedir)

# note: this line is matched against to check that this is a buildmaster
# directory; do not edit it.
application = service.Application('buildmaster')


application.setComponent(ILogObserver, FileLogObserver(sys.stdout).emit)

m = BuildMaster(basedir, configfile)
m.setServiceParent(application)
