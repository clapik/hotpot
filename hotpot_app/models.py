from . import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    activated = db.Column(db.Boolean, nullable=False)

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
        self.activated = False


class Posting(db.Model):
    __tablename__ = 'posting'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.String(100), nullable=False)
    # foreign key
    cook_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


class Appointment(db.Model):
    __tablename__ = 'appointment'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # foreign key
    posting_id = db.Column(db.Integer, db.ForeignKey('posting.id'), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
