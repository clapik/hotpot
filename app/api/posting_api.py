__author__ = 'toanngo'
from flask import Blueprint, g, abort, jsonify, request
from ..models import Posting, Users
from .. import db, cache
from .auth_api import login_required

posting_api = Blueprint('posting_api', __name__)


@posting_api.route('/create', methods=['POST'])
@login_required
def create_posting():
    """
    Rest endpoint for creating a posting
    :return:
    """
    # TODO
    pass


def create_posting_helper(description):
    """
    Create a posting for a particular user
    Should not be called directly
    :param description: posting description
    :return: posting object if succesfully created
    """
    posting = Posting(description, g.user.id)
    db.session.add(posting)
    db.session.commit()
    return posting


@posting_api.route('/get_postings', methods=['POST', 'GET'])
@login_required
def get_postings():
    """
    Get the postings
    :return: json object: {'result':[postings]}
    """
    # default to query all
    query = 'all' if request.method == 'GET' else {'username': request.json['username']}
    postings = get_postings_helper(query)
    if not postings or len(postings) == 0:
        abort(500)
    result = jsonify_postings(postings)
    return jsonify(result), 201


@cache.memoize(timeout=60)
def get_postings_helper(query):
    """
    Query the postings from DB
    :param query: query
    :return: queried postings
    """
    if query == 'all':
        postings = Posting.query.join(Users).add_columns(Users.username).all()
        return postings
    result = Posting.query.join(Users).add_columns(Users.username)
    for key in query:
        if key == 'username':
            result = result.filter_by(username=query.get('username'))
    return result.all()


@cache.memoize(timeout=60)
def jsonify_postings(postings):
    """
    Jsonify a list of postings
    :param postings: postings
    :return: postings as JSON
    """
    result = []
    for posting in postings:
        result.append({
            'id': posting[0].id,
            'description': posting[0].description,
            'cook_id': posting[0].cook_id,
            'cook_username': posting[1]
        })
    return {'result': result}

