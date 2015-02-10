__author__ = 'toanngo'
from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.assets import Environment

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
from .views.profile import profile
from .api.user_api import api

app.register_blueprint(api, url_prefix='/api')


# Register static assets
from .util.assets import bundles

assets = Environment(app)
assets.register(bundles)


@app.route('/')
def blank():
    return render_template('home/login.html')


if __name__ == '__main__':
    app.run()