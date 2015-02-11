__author__ = 'toanngo'
from ..models import Users
from flask import g, Blueprint, make_response, render_template, redirect, url_for
from .. import app

auth_api = Blueprint('auth', __name__, url_prefix='/api/auth')


# @auth_api.route('/verify_password')
def verify_password(email, password):
    print('verify email/password:', email, password)
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
    print('Get auth token')
    token = g.user.generate_auth_token(app)
    res = make_response(redirect(url_for('home.home_page')))
    res.set_cookie('token', token, expires=600)
    return res


def verify_token(token):
    print('verify token:', token)
    # first authenticate token
    user = Users.verify_auth_token(app, token)
    if not user:
        return False
    g.user = user
    return True