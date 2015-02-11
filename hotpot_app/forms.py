__author__ = 'toanngo'
from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import Email, DataRequired


class EmailPasswordForm(Form):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])