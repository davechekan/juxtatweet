import base_config

db_user     =  'juxtatweet'
db_pass     =  'vnFr0z3n*c4Vem4N&L4wy3R'
db_host     =  'FIXME'
db_database =  'juxtatweet'

local_conf = {
    'SQLALCHEMY_DATABASE_URI'   : 'mysql://%s:%s@%s/%s' % (db_user, db_pass, db_host, db_database),

    'db_user'     :  db_user,
    'db_pass'     :  db_pass,
    'db_host'     :  db_host,
    'db_database' :  db_database,
}

conf = base_config.merge_with_base(local_conf)
