import os

PATTERN = r'^[a-zA-Z0-9]{1,16}$'
API_FIELDS = {
    'url': 'original',
    'custom_id': 'short',
}


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URI', default='sqlite:///db.sqlite3'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', default='Secret_Key')
