from database import db

class URLList(db.Model):
    __tablename__ = 'url_list'

    url_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    url = db.Column(db.Text)

    def __repr__(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class ScrapedData(db.Model):
    __tablename__ = 'scraped_data'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    headline = db.Column(db.Text)
    scrape_time = db.Column(db.Date, default=datetime.now())
    outrage_rank = db.Column(db.Integer)

    def __repr__(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
