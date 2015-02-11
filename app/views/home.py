from flask import Blueprint, render_template, request, url_for, redirect, flash, make_response
from ..api.auth_api import verify_token, verify_password, get_auth_token
from ..forms import LoginForm

home = Blueprint('home', __name__)


@home.route('/')
def home_page():
    token = request.cookies.get('token')
    if token and verify_token(token):
        return render_template('home/layout.html')
    return redirect(url_for('home.login'))


@home.route('/login', methods=['POST', 'GET'])
def login():
    token = request.cookies.get('token')
    if token and verify_token(token):
        return redirect(url_for('home.home_page'))
    form = LoginForm()
    if form.validate_on_submit():
        if verify_password(form.email.data, form.password.data):
            return get_auth_token()
        else:
            flash('Invalid email or password')
    return render_template('auth/login.html', form=form)


@home.route('/logout', methods=['POST'])
def logout():
    res = make_response(render_template('auth/logout.html'))
    res.set_cookie('token', '')
    return res