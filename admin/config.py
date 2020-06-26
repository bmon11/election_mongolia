import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = 'LczRxnZNyWWgbkaA5rD'
    SQLALCHEMY_DATABASE_URI = 'mysql://elec:NNaaBBaaRR@133.18.209.124:3306/election?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = False