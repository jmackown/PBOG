from flask import Blueprint, Flask
from database import db
from create_db import ragnarok_bp
from blueprints import main_bp, pres_bp

def create_app():

    app = Flask(__name__,  static_url_path='/static')

    app.config.from_object('default_settings')


    app.register_blueprint(ragnarok_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(pres_bp)

    db.init_app(app)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True,host='0.0.0.0', port='5000')