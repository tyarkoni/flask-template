from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from slimish_jinja import SlimishExtension

from .config import settings
from .config.assets import init_assets

APP_NAME = 'my_app'

app = Flask(APP_NAME, static_folder=settings.STATIC_FOLDER,
            template_folder=settings.TEMPLATE_FOLDER)

db = SQLAlchemy()
_blueprints = []


def setup_logging(logging_path, level):
    '''Setups logging in app'''
    from logging.handlers import RotatingFileHandler
    from logging import getLogger, getLevelName
    file_handler = RotatingFileHandler(logging_path)
    file_handler.setLevel(getLevelName(level))
    loggers = [app.logger, getLogger('sqlalchemy')]
    for logger in loggers:
        logger.addHandler(file_handler)


def create_app(debug=False):
    '''creates app instance, db instance, and apimanager instance'''

    # Extra config stuff
    app.config['DEBUG'] = debug

    # Generate DB URI
    if settings.SQL_ADAPTER == 'sqlite':
        db_uri = settings.SQLALCHEMY_SQLITE_URI
    elif settings.SQL_ADAPTER == 'mysql':
        db_to_use = settings.MYSQL_DEVELOPMENT_DB if settings.DEBUG \
            else settings.MYSQL_PRODUCTION_DB
        db_uri = 'mysql://%s:%s@localhost/%s' % (
            settings.MYSQL_USER, settings.MYSQL_PASSWORD, db_to_use)
    else:
        raise ValueError(
            "Value of SQL_ADAPTER in settings must be either 'sqlite'"
            " or 'mysql'")

    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.debug = True
    app.secret_key = "shhhhhhh"
    app.test_request_context().push()
    db.init_app(app)

    # Add slim support
    Flask.jinja_options['extensions'].append(SlimishExtension)

    # Initialize assets
    init_assets(app)

    # load blueprints
    register_blueprints()


def add_blueprint(blueprint):
    _blueprints.append(blueprint)


def register_blueprints():
    # creates and registers blueprints
    import my_app.controllers.home

    for blueprint in _blueprints:
        app.register_blueprint(blueprint)
