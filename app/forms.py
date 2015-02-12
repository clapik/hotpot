__author__ = 'toanngo'
from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import Email, DataRequired, Length


class EmailPasswordForm(Form):
    email = StringField('Email', validators=[DataRequired(), Email(), Length(1, 64)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField()


class LoginForm(EmailPasswordForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64)])
    remember_me = BooleanField('Keep me logged in')


class RegisterForm(EmailPasswordForm):
    username = StringField('Email', validators=[DataRequired(), Length(1, 64)])


class NewPostingForm(Form):
    description = StringField('Description', validators=[DataRequired(), Length(1, 255)])
    submit = SubmitField()