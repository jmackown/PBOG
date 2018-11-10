import os

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

SECRET_KEY = 'my precious'

DEV_SERVER_HOST = '0.0.0.0'
DEV_SERVER_PORT = 5000


SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = f"postgresql://outrage_db:5432/postgres"
SQLALCHEMY_ECHO = True
