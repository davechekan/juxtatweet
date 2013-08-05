
base_conf = {

    'memcache_address': ['localhost:11211'],

    'SQLALCHEMY_ECHO'           : False,

    'EXCEPTIONAL_API_KEY'            : 'fc316cc0a2ddfdb4952e1ba6586e217f12b22b3d',
    'EXCEPTIONAL_PARAMETER_FILTER'   : ['password', 'password_confirm', 'passwd', 'auth_login', 'session'],
    'EXCEPTIONAL_SESSION_FILTER'     : ['password', 'password_confirm', 'passwd', 'auth_login', 'session'],

    # keep this stuff out of the web interface
    'EXCEPTIONAL_ENVIRONMENT_FILTER' : [
            'USER_DB_USER',
            'USER_DB_PASS',
            'USER_DB_HOST',
            'USER_DB_DATABASE',
            'DATA_DB_USER',
            'DATA_DB_PASS',
            'DATA_DB_HOST',
            'DATA_DB_DATABASE',

            'SQLALCHEMY_DATABASE_URI',

            'GEOCODER_KEY',
            'GMAP_KEY',
            'SECRET_KEY',
            'SSO_KEY',
            'EXCEPTIONAL_API_KEY',

            'MAIL_USERNAME',
            'MAIL_PASSWORD',
    ],
}

def merge_with_base(local_conf):
    """
    Merge the local config with the base config, making sure the
    local config variables override the base config. Return the
    merged dictionary.
    """
    conf = base_conf.copy()
    conf.update(local_conf)

    return conf
