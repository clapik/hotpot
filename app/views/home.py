from flask import render_template, redirect, url_for, Blueprint, session, flash
from ..forms import EmailPasswordForm

home = Blueprint('home', __name__, template_folder='templates', static_folder='static')


@home.route('/login', methods=['GET', 'POST'])
def login():
    form = EmailPasswordForm()
    if form.validate_on_submit():
        # TODO validate user & password
        if session.get('email') is not None:
            flash('oops! email detected')
        return redirect(url_for('home.login'))
    return render_template('home/login.html', form=form)