__author__ = 'toanngo'
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.assets import Environment
from flask_bootstrap import Bootstrap
from flask_cache import Cache

app = Flask(__name__, instance_relative_config=True)

# Load dev config (default)
app.config.from_object('config.default')

# Load config from instance folder
app.config.from_pyfile('config.py')

# Load file specified by APP_CONFIG
app.config.from_envvar('APP_CONFIG')

# Register db
db = SQLAlchemy(app)

from .models import *

# Allow caching
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

# Register Blueprints
from .views.home import home
from .api.user_api import user_api
from .api.auth_api import auth_api
from .api.posting_api import posting_api

app.register_blueprint(home)
app.register_blueprint(user_api, url_prefix='/api/user')
app.register_blueprint(auth_api, url_prefix='/api/auth')
app.register_blueprint(posting_api, url_prefix='/api/posting')

# Register static assets
from .util.assets import bundles

assets = Environment(app)
assets.register(bundles)

# Register Boostrap
bootstrap = Bootstrap(app)

app.secret_key = app.config['SECRET_KEY']

if __name__ == '__main__':
    app.run()