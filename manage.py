__author__ = 'toanngo'
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from app import app, db

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

# manager.add_command('app', app.run)

"""
python manage.py
db init         - initialize Alembic
db migrate      - first migration
db upgrade      - apply changes (upgrade)
"""
if __name__ == '__main__':
    manager.run()
