__author__ = 'toanngo'
from flask import Flask
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

if __name__ == '__main__':
    app.run()