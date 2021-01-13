import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """Site configuration"""
    SECRET_KEY = 'Try-to-gue$$'
    FLASK_APP = 'app.py'
