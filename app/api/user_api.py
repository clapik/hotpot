__author__ = 'toanngo'
from flask import request, abort, jsonify, make_response, Blueprint
from ..models import Users
from .auth_api import login_required, user_required
from .. import db

user_api = Blueprint('user_api', __name__)


@user_api.route('/', methods=['GET'])
def home():
    # TODO
    return 'USER API Home!'


@user_api.route('/register', methods=['POST'])
def register_user():
    """
    Rest endpoint to register user
    :return: username if success
    """
    username = request.json['username']
    password = request.json['password']
    email = request.json['email']
    if username is None or password is None or email is None:
        abort(400)
    user = register_new_user(username, email, password)
    if not user:
        abort(400)
    return jsonify({'user': user.username}), 201


def register_new_user(username, email, password):
    """
    Register a new user if not exist
    :param username: username
    :param email: email
    :param password: password
    :return: new user if exists
    """
    if Users.query.filter_by(username=username).first() is not None:
        return None
    if Users.query.filter_by(email=email).first() is not None:
        return None
    user = Users(username=username, password=password, email=email)
    db.session.add(user)
    db.session.commit()
    return user


@user_api.route('/delete/<username>', methods=['POST'])
@login_required
def delete_user(username):
    # TODO
    pass


@user_required
def delete_user_helper(username):
    # TODO
    pass


@user_api.route('/edit', methods=['POST'])
@login_required
def edit_user():
    # TODO
    pass


@user_required
def edit_user_helper(username):
    # TODO
    pass


@user_api.route('/find_user/{username}')
@login_required
def find_user(username):
    # TODO
    pass


def find_user_helper(username):
    # TODO
    pass
