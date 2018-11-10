from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from database import db

def create_app():

    app = Flask(__name__)

# app = Flask(__name__)

    @app.route('/')
    def hello_world():
        return 'Flask Dockerized'


    db.init_app(app)


    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True,host='0.0.0.0', port='5000')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port='5000')