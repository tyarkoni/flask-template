from os.path import join, dirname, realpath, pardir

APP_NAME = 'my_app'

DEBUG = True

# Paths
ROOT_DIR = realpath(join(join(dirname(__file__), pardir), pardir))
DATA_DIR = join(ROOT_DIR, 'data')
STATIC_FOLDER = join(ROOT_DIR, APP_NAME, 'static')
TEMPLATE_FOLDER = join(ROOT_DIR, APP_NAME, 'templates')

### DATABASE CONFIGURATION ###
# Adapter to use--either 'mysql' or 'sqlite'
SQL_ADAPTER = 'mysql'

# SQLite path
SQLALCHEMY_SQLITE_URI = 'sqlite:///' + DATA_DIR + 'data.db'

# MySQL configuration
MYSQL_USER = 'meep'
MYSQL_PASSWORD = 'meep'
MYSQL_PRODUCTION_DB = 'meep'
MYSQL_DEVELOPMENT_DB = 'meep'

# Logging
LOGGING_PATH = join(ROOT_DIR, 'log.txt')
LOGGING_LEVEL = 'DEBUG'
