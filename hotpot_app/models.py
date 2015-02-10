from . import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    type = db.Column(db.String(20))
    __mapper_args__ = {'polymorphic_on': type}


class Cook(User):
    __tablename__ = 'cook'
    id = db.Column(None, db.ForeignKey('user.id'), primary_key=True)
    __mapper_args__ = {'polymorphic_identity': 'cook'}


class Customer(User):
    __tablename__ = 'customer'
    id = db.Column(None, db.ForeignKey('user.id'), primary_key=True)
    __mapper_args__ = {'polymorphic_identity': 'customer'}


class Posting(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.String(100), nullable=False)
    # foreign key
    cook_id = db.Column(db.Integer, db.ForeignKey('cook.id'), nullable=False)


class Appointment(db.Model):
    __tablename__ = 'appointment'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # foreign key
    posting_id = db.Column(db.Integer, db.ForeignKey('posting.id'), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
