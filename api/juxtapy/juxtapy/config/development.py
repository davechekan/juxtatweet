import base_config

db_driver   =  'postgresql+psycopg2'
db_file     =  '/tmp/dev.db'
db_user     =  'juxtatweet'
db_pass     =  'vnFr0z3n*c4Vem4N&L4wy3R'
db_host     =  'localhost'
db_database =  'juxtatweet'

local_conf = {
    # dev
    'SQLALCHEMY_DATABASE_URI'   : '%s://%s:%s@%s/%s' % (db_driver, db_user, db_pass, db_host, db_database),
    #'SQLALCHEMY_DATABASE_URI'   : '%s:///%s' % (db_driver, db_file),

    'INFO_LOG'  : '/tmp/info.log',
    'WARN_LOG'  : '/tmp/warn.log',
    'ERROR_LOG' : '/tmp/error.log',

    'db_user'     :  db_user,
    'db_pass'     :  db_pass,
    'db_host'     :  db_host,
    'db_database' :  db_database,
}

conf = base_config.merge_with_base(local_conf)
