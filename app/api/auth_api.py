__author__ = 'toanngo'
from ..models import Users
from flask import g, Blueprint, make_response, redirect, url_for, request, session
from .. import app
from functools import wraps

auth_api = Blueprint('auth', __name__, url_prefix='/api/auth')


# @auth_api.route('/verify_password')
def verify_password(email, password):
    # try to authenticate username and password
    user = Users.query.filter_by(email=email).first()
    if not user or not user.verify_password(password):
        return False
    g.user = user
    return True


@auth_api.route('/token')
def get_auth_token():
    """
    get auth token
    :return: token
    """
    token = g.user.generate_auth_token(app)
    res = make_response(redirect(request.args.get('next') or url_for('home.home_page')))
    session['token'] = token
    return res


def verify_token(token):
    user = Users.verify_auth_token(app, token)
    if not user:
        return False
    g.user = user
    return True


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'token' in session and session['token']:
            token = session['token']
            print('login_required - token:', token)
            if not token or not verify_token(token):
                return redirect(url_for('home.login', next=request.url))
        else:
            return redirect(url_for('home.login', next=request.url))
        return f(*args, **kwargs)

    return decorated_function