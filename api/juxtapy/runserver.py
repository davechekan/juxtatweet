#!/usr/bin/env python

import sys

from juxtapy import app

if __name__ == '__main__':

    # default to unprivileged port, but it can be changed
    # by passing a port number as first arg to the script
    port = 5001
    if len(sys.argv) > 1:
        port = int(sys.argv[1])

    debug = True if app.debug else False
    app.run(host='0.0.0.0', port=port, debug=debug, threaded=True)
