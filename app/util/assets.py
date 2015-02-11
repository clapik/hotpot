__author__ = 'toanngo'
from flask.ext.assets import Bundle, Environment

from .. import app

bundles = {
    'login_js': Bundle('js/login.js',
                       output='gen/login.js')
}

assets = Environment(app)
assets.register(bundles)