#!/usr/bin/env python

import sys
import os

env = len(sys.argv) > 1 and sys.argv[1]

allowed_envs = ['testing',
                'development',
                'integration',
                'staging',
                'production',
               ]

if env not in allowed_envs:
    print "Require first arg in [%s]" % ', '.join(allowed_envs)
    sys.exit()

print "Setting env to %s" % env

script_dir = os.path.dirname(__file__)
filename = '%s/%s' % (script_dir, '../juxtapy/config/env.py')

s = 'env="%s"' % env

fh = open(filename, 'wb')
fh.write(s)
fh.close()
