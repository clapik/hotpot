import os

DEBUG = True
BCRYPT_LEVEL = 12

MAIL_SERVER = 'smtp.googlemail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
MAIL_SUBJECT_PREFIX = '[HotPot]'
MAIL_SENDER = 'HotPot Admin <toanngo-dev@gmail.com>'