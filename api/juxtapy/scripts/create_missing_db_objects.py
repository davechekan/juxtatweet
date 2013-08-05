#!/usr/bin/env python

# HACK - might have to change this if the script moves...
import sys
sys.path.append('..')

import juxtapy
import juxtapy.model as model

juxtapy.db.create_all()
