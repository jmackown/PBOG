from flask import Blueprint, Flask
from flask_sqlalchemy import SQLAlchemy
from create_db import ragnarok_bp

from database import db

def create_app():

    app = Flask(__name__)

    app.config.from_object('default_settings')

    @app.route('/')
    def hello_world():
        return 'Flask Dockerized'


    db.init_app(app)

    app.register_blueprint(ragnarok_bp)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True,host='0.0.0.0', port='5000')