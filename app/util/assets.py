__author__ = 'toanngo'
from flask.ext.assets import Bundle, Environment

from .. import app

bundles = {
    'login_js': Bundle('js/login.js', output='gen/login.js'),
    'login_css': Bundle('css/login.css', output='gen/login.css'),
    'dashboard_js': Bundle('js/lib/docs.min.js', output='gen/dashboard.js'),
    'dashboard_css': Bundle('css/dashboard.css', output='gen/dashboard.css')
}

assets = Environment(app)
assets.register(bundles)