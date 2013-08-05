import os
import importlib

from .env import env

module_path = 'juxtapy.config'

def update_config(app):
    """
    Update the config in the app object. Based on the value in the
    env.py file, we decide which config module to read from.
    """

    juxtapy_env = env

    # you can override the environment with a environment variable
    environ_env = os.environ.get('JUXTAPY_ENV')
    if environ_env:
        juxtapy_env = environ_env

    app.juxtapy_env = juxtapy_env

    conf = get_config_for_env(juxtapy_env)

    for key, val in conf.iteritems():
        app.config[key] = val

def get_config_for_env(juxtapy_env):
    """
    """
    _env = juxtapy_env.replace('-', '_')

    to_be_imported = '%s.%s' % (module_path, _env)

    config = importlib.import_module(to_be_imported)

    return config.conf
