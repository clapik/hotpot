from flask import Flask

app = Flask(__name__, instance_relative_config=True)

# Load dev config (default)
app.config.from_object('config.dev')

# Load config from instance folder
app.config.from_pyfile('config.py')

# Load file specified by APP_CONFIG
app.config.from_envvar('APP_CONFIG')

print(app.config['SQLALCHEMY_DATABASE_URI'])
