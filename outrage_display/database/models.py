from database import db
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy


class URLList(db.Model):
    __tablename__ = 'url_lists'

    url_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text)
    url = db.Column(db.Text)

    def __repr__(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class ScrapedData(db.Model):
    __tablename__ = 'scraped_data'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    source = db.Column(db.Text)
    headline = db.Column(db.Text)
    scrape_time = db.Column(db.TIMESTAMP, default=datetime.now())
    outrage_rank = db.Column(db.Integer)

    def __repr__(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
