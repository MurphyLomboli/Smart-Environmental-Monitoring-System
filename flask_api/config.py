import os
basedir = os.path.abspath(os.path.dirname(__file__))

class config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
            'sqlite:///' + os.path.join(basedir, 'sems.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
