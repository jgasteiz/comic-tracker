from .common import *

import dj_database_url

SECRET_KEY = os.environ['SECRET_KEY']

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)
