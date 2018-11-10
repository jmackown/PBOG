from database import db
from flask import Blueprint
from database.models import URLList, ScrapedData

ragnarok_bp = Blueprint('ragnarok', __name__)


@ragnarok_bp.route('/ragnarok/', methods=['GET'])
def ragnarok():

    db.session.close()
    db.drop_all()
    db.create_all()
    db.session.commit()

    return "NUKED!! ☢ (and rebuilt database)"
