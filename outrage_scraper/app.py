import atexit

from apscheduler.schedulers.background import BackgroundScheduler
from scraper import Scraper
from flask import Flask

app = Flask(__name__)

scraper = Scraper()

scheduler = BackgroundScheduler()
scheduler.add_job(func=scraper.scrape, trigger="interval", seconds=60)
scheduler.start()

atexit.register(lambda: scheduler.shutdown())

if __name__ == '__main__':
    app.run(port='66')
