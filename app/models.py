from . import db
from flask.ext.login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, SignatureExpired, BadSignature
from passlib.apps import custom_app_context as pwd_context
import datetime


class Users(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    activated = db.Column(db.Boolean, nullable=False)
    fname = db.Column(db.String(40))
    lname = db.Column(db.String(40))

    def __init__(self, username='', password='', email='', fname='', lname=''):
        self.username = username
        self.password = pwd_context.encrypt(password)
        self.email = email
        self.activated = False
        self.fname = fname
        self.lname = lname

    def verify_password(self, password):
        return pwd_context.verify(password, self.password)

    def generate_auth_token(self, app, expiration=600):
        s = Serializer(app.config['SECRET_KEY'], expires_in=expiration)
        return s.dumps({'id': self.id})

    @staticmethod
    def verify_auth_token(app, token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except SignatureExpired or BadSignature:
            return None
        user = Users.query.get(data['id'])
        return user


class Posting(db.Model):
    __tablename__ = 'posting'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float)
    date = db.Column(db.DateTime)
    # TODO add more fields
    # foreign key
    cook_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __init__(self, description='', price=0, date=datetime.date.today(), cook_id=''):
        self.description = description
        self.price = price
        self.date = date
        self.cook_id = cook_id


class Appointment(db.Model):
    __tablename__ = 'appointment'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # foreign key
    posting_id = db.Column(db.Integer, db.ForeignKey('posting.id'), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __init__(self, posting_id=0, customer_id=0):
        self.posting_id = posting_id
        self.customer_id = customer_id