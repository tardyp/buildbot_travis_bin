from buildbot_travis import TravisConfigurator
from buildbot.plugins import buildslave
import os

c = BuildmasterConfig = {}
c['slavePortnum'] = 19989

if 'DB_URL' in os.environ:
    c['db_url'] = os.environ['DB_URL']

c['slaves'] = []
for i in xrange(int(os.environ.get("NUM_SLAVES", 1))):
    c['slaves'].append(buildslave.BuildSlave('slave%d' % (i,), 'pass'))
TravisConfigurator(BuildmasterConfig, basedir).fromDb()
