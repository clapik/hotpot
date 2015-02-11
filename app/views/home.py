from flask import Blueprint, render_template, request, url_for, redirect, flash, session
from ..api.auth_api import verify_token, verify_password, get_auth_token, login_required
from ..forms import LoginForm

home = Blueprint('home', __name__)


@home.route('/')
@login_required
def home_page():
    return render_template('home/layout.html')


@home.route('/login', methods=['POST', 'GET'])
def login():
    if 'token' in session:
        token = session['token']
        print('login - token:', token)
        if token and verify_token(token):
            return redirect(url_for(request.args.get('next')) or url_for('home.home_page'))
    form = LoginForm()
    if form.validate_on_submit():
        if verify_password(form.email.data, form.password.data):
            return get_auth_token()
        else:
            flash('Invalid email or password')
    return render_template('auth/login.html', form=form)


@home.route('/logout', methods=['POST'])
def logout():
    session.pop('token', None)
    return redirect(url_for('home.home_page'))