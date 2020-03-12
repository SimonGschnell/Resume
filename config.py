import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY= os.environ.get('SECRET_KEY') or 'Passwort5!'
    SQLALCHEMY_DATABASE_URI= os.environ.get('DATABASE_URL') or 'sqlite:///'+os.path.join(basedir,'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'smtp.googlemail.com'
    Mail_PORT = int(os.environ.get('MAIL_PORT')or 587)
    MAIL_USE_TLS = 1
    MAIL_USERNAME = 'icecubethe3@gmail.com'
    MAIL_PASSWORD = 'Passwort5!'
    ADMINS = ['icecubethe3@gmail.com']
    POSTS_PER_PAGE=25
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')
    MY_MAIL=['simongschnell@gmail.com']