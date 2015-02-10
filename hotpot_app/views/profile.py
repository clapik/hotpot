from flask import Blueprint, render_template, g
# from ..models import *

profile = Blueprint('profile', __name__, template_folder='templates', static_folder='static')


@profile.url_value_preprocessor
def get_profile_owner(endpoint, values):
    pass
    # query = User.query.filter_by(username=values.pop('username'))
    # g.profile_owner = query.first_or_404()


@profile.route('/')
def timeline():
    return render_template('profile/timeline.html')


@profile.route('/postings')
def postings():
    return render_template('profile/postings.html')


@profile.route('/about')
def about():
    return render_template('profile/about.html')