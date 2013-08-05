# build a config dictionary
import base_config

sql_url = 'sqlite://'

local_conf = {
    'SQLALCHEMY_DATABASE_URI'   : sql_url,
}

conf = base_config.merge_with_base(local_conf)
