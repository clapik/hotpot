from flask import Blueprint, render_template, request, url_for, redirect, flash, session, g, abort, send_from_directory
from ..api.auth_api import verify_token, verify_password, get_auth_token, login_required, user_required
from ..api.user_api import register_new_user
from ..api.posting_api import create_posting_helper
from ..forms import LoginForm, RegisterForm, NewPostingForm
import os

home = Blueprint('home', __name__)


@home.route('/')
@login_required
def home_page():
    return redirect(url_for('home.home_page') + g.user.username)


@home.route('/login', methods=['POST', 'GET'])
def login():
    if 'token' in session:
        token = session['token']
        if token and verify_token(token):
            if 'next' in request.args:
                return redirect(url_for(request.args.get('next')))
            return redirect(url_for('home.home_page'))
    form = LoginForm()
    if form.validate_on_submit():
        if verify_password(form.email.data, form.password.data):
            return get_auth_token()
        else:
            flash('Invalid email or password')
    return render_template('home/login.html', form=form)


@home.route('/logout', methods=['POST'])
def logout():
    session.pop('token', None)
    return redirect(url_for('home.home_page'))


@home.route('/register', methods=['POST', 'GET'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = register_new_user(username=form.username.data, password=form.password.data, email=form.email.data)
        if user:
            return redirect(url_for('home.login'))
        flash('Username/Email exists')
        form = RegisterForm()
    return render_template('home/register.html', form=form)


@home.route('/<username>')
@login_required
@user_required
def dashboard(username):
    return render_template('home/dashboard/dashboard.html', username=username)


@home.route('/<username>/create_posting', methods=['POST', 'GET'])
@login_required
@user_required
def create_posting(username):
    form = NewPostingForm()
    if form.validate_on_submit():
        posting = create_posting_helper(form.description.data)
        flash('Posting created! Unique posting id: ' + str(posting.id))
        return redirect(url_for('home.home_page'))
    return render_template('home/create_posting.html', form=form, username=username)


@home.route('/favicon.ico')
def favicon():
    """
    serve favicon.ico
    :return: serve favicon.ico
    """
    return send_from_directory(os.path.join(home.root_path, 'static'), 'favicon.ico')
