__author__ = 'toanngo'
from flask import Blueprint, g, abort, jsonify
from ..models import Posting, Users
from .. import db
from .auth_api import login_required

posting_api = Blueprint('posting_api', __name__)


@posting_api.route('/create', methods=['POST'])
@login_required
def create_posting():
    # TODO
    pass


def create_posting_helper(description):
    posting = Posting(description, g.user.id)
    db.session.add(posting)
    db.session.commit()
    return posting


@posting_api.route('/get_postings', methods=['POST', 'GET'])
@login_required
def get_postings():
    # default to query all
    postings = get_postings_helper()
    if not postings or len(postings) == 0:
        abort(500)
    result = jsonify_postings(postings)
    return jsonify(result), 201
    # TODO add option to query specific


def get_postings_helper(query='all'):
    if query == 'all':
        postings = Posting.query.join(Users).add_columns(Users.username).all()
        return postings
    else:
        return None


def jsonify_postings(postings):
    result = []
    for posting in postings:
        result.append({
            'id': posting[0].id,
            'description': posting[0].description,
            'cook_id': posting[0].cook_id,
            'cook_username': posting[1]
        })
    return {'result': result}

