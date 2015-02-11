__author__ = 'toanngo'
from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.assets import Environment
from flask_bootstrap import Bootstrap

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

# Register Blueprints
from .views.home import home
from .api.user_api import user_api
from .api.auth_api import auth_api

app.register_blueprint(home)
app.register_blueprint(user_api, url_prefix='/api/user')
app.register_blueprint(auth_api, url_prefix='/api/auth')

# Register static assets
from .util.assets import bundles

assets = Environment(app)
assets.register(bundles)

# Register Boostrap
bootstrap = Bootstrap(app)

if __name__ == '__main__':
    app.run()