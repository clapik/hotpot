from flask import render_template, redirect, url_for, Blueprint
from ..forms import EmailPasswordForm

login = Blueprint('login', __name__, template_folder='templates', static_folder='static')


@login.route('/login', methods=['GET', 'POST'])
def login_f():
    form = EmailPasswordForm()
    if form.validate_on_submit():
        # TODO check password
        return redirect(url_for('index'))
    return render_template('home/login.html', form=form)