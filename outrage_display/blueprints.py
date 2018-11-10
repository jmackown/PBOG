from database import db
from flask import Blueprint, render_template
from database.models import URLList, ScrapedData

main_bp = Blueprint('index', __name__)


@main_bp.route('/', methods=['GET'])
def index():
    return render_template('index.html')