__author__ = 'toanngo'
from ..models import Users
from flask import g, Blueprint, make_response, redirect, url_for, request, session, abort
from .. import app
from functools import wraps

auth_api = Blueprint('auth', __name__, url_prefix='/api/auth')


def verify_password(email_or_username, password):
    """
    compare the password received and the password in database
    :param email_or_username: email/username
    :param password: password
    :return: boolean
    """
    user = Users.query.filter_by(email=email_or_username).first()
    if not user or not user.verify_password(password):
        user = Users.query.filter_by(username=email_or_username).first()
        if not user:
            return False
    g.user = user
    return True


@auth_api.route('/token')
def get_auth_token(remember_me=False):
    """
    get auth token IFF successfully logged in
    token lasts for ~ 5 days if remember_me
    else 1h
    :return: token
    """
    expiration = 400000 if remember_me else 3600
    token = g.user.generate_auth_token(app, expiration=expiration)
    res = make_response(redirect(request.args.get('next') or url_for('home.home_page')))
    session['token'] = token
    return res


def verify_token(token):
    """
    Verify a token (validity and expiration) against db
    :param token: token
    :return: boolean
    """
    user = Users.verify_auth_token(app, token)
    if not user:
        return False
    g.user = user
    return True


def login_required(f):
    """
    wrapper function to enforce login
    :param f: function being wrapped
    :return: check token's validity
    """

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'token' in session and session['token']:
            token = session['token']
            if not token or not verify_token(token):
                return redirect(url_for('home.login', next=request.url))
        else:
            return redirect(url_for('home.login', next=request.url))
        return f(*args, **kwargs)

    return decorated_function


def user_required(f):
    """
    wrapper function to enforce the right username
    :param f: function being wrapped, with parameter 'username' passed in
    :return: check username against token
    """

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' in kwargs:
            username = kwargs.get('username')
            if username == g.user.username:
                return f(*args, **kwargs)
            else:
                abort(403)
        else:
            abort(403)

    return decorated_function