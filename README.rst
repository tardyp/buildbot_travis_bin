Buildbot Travis binaries
========================

This repository hold a easy to install buildbot travis


Usage
=====

::
    virtualenv sandbox
    . ./sandbox/bin/activate
    pip install -r requirements.txt
    pip install honcho
    honcho start

Supervisord generation
======================

::

    honcho export supervisord supervisord -l /var/log/travis -u travisuser -s /bin/sh 

.env file
=========

Application is fully configured via .env. known keys:

* NUM_SLAVES: number of slaves configured. They are all on the same machine, and running on the same twisted process
* DB_URL: url to the mysql or postgresql database. If unset, then sqlite is used
* buildbotURL: url where your bot is visible

That's it..

Rest of the configuration happens in the UI. (thus dont need to be documented :) )

Configuration with nginx reverse proxy
======================================
Make sure you have following nginx config in the same machine as buildbot::

        location /travis/ {
            proxy_buffering off;
            proxy_pass http://localhost:5000/;
        }

Authentication
==============
For the moment, authentication is not supported, all users can change the configuration in the UI

