__author__ = 'toanngo'
from flask import request, abort, jsonify, make_response, Blueprint, g
from ..models import Posting
from .. import db
from .auth_api import login_required

posting_api = Blueprint('user_api', __name__)


@posting_api.route('/create')
@login_required
def create_posting():
    # TODO
    pass


def create_posting_helper(description):
    posting = Posting(description, g.user.id)
    db.session.add(posting)
    db.session.commit()
    return posting