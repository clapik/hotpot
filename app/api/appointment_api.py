__author__ = 'toanngo'
from flask import Blueprint, g, abort, jsonify, request, flash
from ..models import Appointment, Users, Posting
from .. import db, cache
from .auth_api import login_required, user_required

appointment_api = Blueprint('appointment_api', __name__)


@appointment_api.route('/create', methods=['POST'])
@login_required
def create_appointment():
    """
    Rest endpoint for creating a appointment
    consumes a posting in json format
    :return:
    """
    appointment = create_appointment_helper(g.user, request.json['id'])
    if not appointment:
        abort(500)
    return jsonify({
        'appointment_id': appointment.id,
        'posting_id': appointment.posting_id,
        'customer_id': appointment.customer_id
    }), 201


def create_appointment_helper(user, posting_id):
    posting = Posting.query.join(Users).add_columns(Users.username).filter(Posting.id == posting_id).first()
    posting_owner = posting[1]
    if user.username == posting_owner:
        return None
    appointment = Appointment(posting_id, user.id)
    db.session.add(appointment)
    db.session.commit()
    return appointment


@appointment_api.route('/get_appointments', methods=['POST', 'GET'])
@login_required
def get_appointments():
    """
    Get the appointments
    :return:
    """
    query = 'all'
    appointments = get_appointments_helper_cache(g.user, query)
    if not appointments:
        abort(500)
    return jsonify(appointments), 201


@cache.memoize(timeout=60)
def get_appointments_helper_cache(user, query):
    return get_appointments_helper(user, query)


def get_appointments_helper(user, query='all'):
    if query == 'all':
        appointments = db.engine.execute(
            'select appointment.id, posting.id, posting.description, posting.price, posting.date ,cook.username, cust.username'
            ' from appointment, posting, users cook, users cust'
            ' where appointment.posting_id = posting.id and cook.id=posting.cook_id and appointment.customer_id = cust.id'
            ' and cust.id=' + str(user.id))
        return jsonify_appointments(appointments)


@appointment_api.route('/edit_appointment/<appointmentid>', methods=['POST'])
@login_required
def edit_appointment(appointmentid):
    # TODO
    pass


@user_required
def edit_appointment_helper(appointmentid, username):
    # TODO
    pass


@appointment_api.route('/delete', methods=['POST'])
@login_required
def delete_appointment():
    customer_id = Appointment.query.filter_by(id=request.json['id']).first().customer_id
    customer = Users.query.filter_by(id=customer_id).first()
    appointment = delete_appointment_helper(request.json['id'], username=customer.username)
    if not appointment:
        abort(500)
    return jsonify({
        'appointment_id': appointment.id,
        'posting_id': appointment.posting_id,
        'customer_id': appointment.customer_id
    }), 201


@user_required
def delete_appointment_helper(appointment_id, username):
    appointment = Appointment.query.filter_by(id=appointment_id).first()
    db.session.delete(appointment)
    db.session.commit()
    return appointment


@cache.memoize(timeout=60)
def jsonify_appointments(appointments):
    result = []
    for appointment in appointments:
        result.append({
            'appointment_id': appointment[0],
            'posting_id': appointment[1],
            'description': appointment[2],
            'price': appointment[3],
            'date': str(appointment[4].month) + '/' + str(appointment[4].day) + '/' + str(
                appointment[4].year),
            'cook_username': appointment[5],
            'customer_username': appointment[6]
        })
    return {'result': result}

