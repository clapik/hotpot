__author__ = 'toanngo'
from flask import request, abort, jsonify, make_response, Blueprint
from ..models import User
from .. import db

api = Blueprint('api', __name__)


@api.route('/', methods=['GET'])
@api.errorhandler(400)
def home():
    # TODO
    return 'API Home!'


@api.route('/user/register', methods=['POST'])
@api.errorhandler(400)
def register_user():
    if not request.json or 'username' not in request.json or 'password' not in request.json:
        abort(400)
    if User.query.filter_by(username=request.json['username']).first() is not None:
        return 'username exists', 201
    user = User(request.json['username'], request.json['password'], request.json['email'])
    db.session.add(user)
    return jsonify({'user': user.username}), 201


@api.errorhandler(400)
def invalid_input(error):
    return make_response(jsonify({'error': 'Invalid Input'}), 400)


@api.errorhandler(400)
def not_found(error):
    return make_response(jsonify({'error': 'Not Found'}), 400)

