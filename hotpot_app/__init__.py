__author__ = 'toanngo'
from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy

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

# app.register_blueprint(profile, url_prefix='/<user_url>')
app.register_blueprint(api, url_prefix='/api')


@app.route('/')
def blank():
    return render_template('home/login.html')


if __name__ == '__main__':
    app.run()