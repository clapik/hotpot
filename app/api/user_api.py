__author__ = 'toanngo'
from flask import request, abort, jsonify, make_response, Blueprint
from ..models import Users
from .. import db

user_api = Blueprint('user_api', __name__)


@user_api.route('/', methods=['GET'])
@user_api.errorhandler(400)
def home():
    # TODO
    return 'USER API Home!'


@user_api.route('/register', methods=['POST'])
@user_api.errorhandler(400)
def register_user():
    """
    Register a User
    :return: username if success
    """
    username = request.json['username']
    password = request.json['password']
    email = request.json['email']
    if username is None or password is None or email is None:
        abort(400)
    if Users.query.filter_by(username=request.json['username']).first() is not None:
        return 'username exists', 201
    user = Users(request.json['username'], request.json['password'], request.json['email'])
    db.session.add(user)
    db.session.commit()
    return jsonify({'user': user.username}), 201


@user_api.errorhandler(400)
def invalid_input(error):
    return make_response(jsonify({'error': 'Invalid Input'}), 400)


@user_api.errorhandler(400)
def not_found(error):
    return make_response(jsonify({'error': 'Not Found'}), 400)

