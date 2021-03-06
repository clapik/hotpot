__author__ = 'toanngo'
from flask.ext.mail import Message, Mail
from threading import Thread
# from flask import render_template
from .. import app

mail = Mail(app)


def send_async_email(msg):
    with app.app_context():
        mail.send(msg)


def send_email(to, subject):  # template, **kwargs):
    msg = Message(app.config['MAIL_SUBJECT_PREFIX'] + subject,
                  sender=app.config['MAIL_SENDER'], recipients=[to])
    # msg.body = render_template(template + '.txt', **kwargs)
    # msg.html = render_template(template + '.html', **kwargs)
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    return thr