__author__ = 'toanngo'
from flask import Blueprint, g, abort, jsonify, request
from ..models import Posting, Users
from .. import db, cache
from .auth_api import login_required, user_required
import datetime

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


def create_posting_helper(json):
    """
    Create a posting for a particular user
    Should not be called directly
    :param json: posting as json dict
    :return: posting object if succesfully created
    """
    posting = Posting(description=json['description'], cook_id=g.user.id, date=json['date'], price=json['price'])
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
    postings = get_postings_helper_cache(query)
    if not postings or len(postings) == 0:
        abort(500)
    result = jsonify_postings(postings)
    return jsonify(result), 201


@cache.memoize(timeout=60)
def get_postings_helper_cache(query):
    return get_postings_helper(query)


def get_postings_helper(query='all'):
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


@posting_api.route('/edit_posting', methods=['POST'])
@login_required
def edit_posting():
    """
    rest api for editing a posting
    :return:
    """
    # get the owner of the posting
    username = Posting.query.join(Users).add_columns(Users.username).filter_by(id=request.json['id']).first()[1]
    new_posting = request.json
    posting = edit_posting_helper_auth(new_posting, username=username)
    if not posting:
        abort(500)
    return 'SUCCESS', 201


@user_required
def edit_posting_helper_auth(new_posting, username):
    return edit_posting_helper(new_posting)


def edit_posting_helper(new_posting):
    """
    edit posting helper
    :param new_posting: new posting info - json format
    date format example: Thursday, 29 March 2015
    :return:
    """
    p = Posting.query.filter_by(id=new_posting['id']).first()
    if not p:
        return None
    if 'description' in new_posting:
        p.description = new_posting['description']
    if 'price' in new_posting:
        if isinstance(new_posting['price'], (float, int)):
            p.price = new_posting['price']
        else:
            return None
    if 'date' in new_posting:
        if isinstance(new_posting['date'], datetime.date):
            p.date = new_posting['date']
        elif isinstance(new_posting['date'], str):
            try:
                value = datetime.datetime.strptime(new_posting['date'], '%m/%d/%Y')
                p.date = value
            except ValueError:
                return None
        else:
            return None
    if 'cook_id' in new_posting:
        p.cook_id = new_posting['cook_id']
    db.session.commit()
    return p


@posting_api.route('/delete_posting/<posting_id>', methods=['POST'])
@login_required
def delete_posting(posting_id):
    """
    rest api for deleting a posting
    :return:
    """
    # get the owner of the posting
    username = Posting.query.join(Users).add_columns(Users.username).first()[1]
    posting = delete_posting_helper_wrapper(posting_id, username=username)
    if not posting:
        abort(500)
    return jsonify(posting), 201


@user_required
def delete_posting_helper_wrapper(posting_id, username):
    return delete_posting_helper(posting_id)


def delete_posting_helper(posting_id):
    p = Posting.query.filter_by(id=posting_id).first()
    db.session.delete(p)
    db.session.commit()
    return p


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
            'price': posting[0].price,
            'date': str(posting[0].date.month) + '/' + str(posting[0].date.day) + '/' + str(posting[0].date.year),
            'cook_username': posting[1]
        })
    return {'result': result}

