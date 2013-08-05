from flask import Flask

app = Flask(__name__)
app.secret_key = '\xc9\xb2Y\xde\xf2\x13o\x8d\xec\x95\xdd\x1c\x92\x9f\xfa]9Y\x8d\xa6\xaa\xe6\x84\x87'

app.debug = True

import juxtapy.config as config
config.update_config(app)

import juxtapy.utils.extension as ext

db = ext.setup_sqlalchemy(app)

import juxtapy.utils.routing as routing
routing.setup(app)                # set up all paths to view funcs
