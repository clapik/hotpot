__author__ = 'toanngo'
from flask.ext.httpauth import HTTPBasicAuth
from ..models import Users
from flask import g, Blueprint, jsonify
from .. import app

auth_api = Blueprint('auth', __name__, url_prefix='/api/auth')
auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(username_or_token, password):
    # first authenticate token
    user = Users.verify_auth_token(app, username_or_token)
    if not user:
        # try to authenticate username n password
        user = Users.query.filter_by(username=username_or_token).first()
        if not user or not user.verify_password(password):
            return False
        g.user = user
        return True


@auth_api.route('/token')
@auth.login_required
def get_auth_token():
    """
    get auth token
    :return: token
    """
    token = g.user.generate_auth_token(app)
    return jsonify({'token': token.decode('ascii'), 'duration': 600})