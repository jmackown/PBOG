from database import db
from flask import Blueprint, render_template
from database.models import URLList, ScrapedData
from  sqlalchemy.sql.expression import func, select
import random


image_sizes = [
    '200',
    '400'
]


main_bp = Blueprint('index', __name__)


@main_bp.route('/', methods=['GET'])
def index():
    headline = ScrapedData.query.all()
    return render_template('index.html', headline = headline, image_sizes=image_sizes)