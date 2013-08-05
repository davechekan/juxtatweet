import os
import sys

# set the env var to override our current gotham_env
os.environ['JUXTAPY_ENV'] = 'testing'

# set the path so that we can import directly from the
# testing dir, without funky relative imports
curr_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(curr_dir)

