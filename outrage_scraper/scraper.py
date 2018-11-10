from bs4 import BeautifulSoup
import requests
import psycopg2


class Scraper:

    def __init__(self):
        self.websites = ("https://thelincolnite.co.uk/",)
        self.website_data = {}

    def scrape(self):
        self.get_content_in_sites()
        self.get_header_tags()

        conn = psycopg2.connect(dbname="outrage", user="postgres", host="outrage_db", port='5432')
        cur = conn.cursor()

        for site in self.website_data:
            for headline in self.website_data[site]['headers']:
                sql = f"INSERT INTO scraped_data (headline, scrape_time) SELECT '{headline}', now() " \
                      f"WHERE NOT EXISTS (SELECT 1 FROM scraped_data WHERE headline = '{headline}');"

                cur.execute(sql)

        conn.commit()
        conn.close()

        return self.website_data

    def get_content_in_sites(self):

        for website in self.websites:

            self.website_data[website] = {}

            r = requests.get(website)

            if r.status_code == 200:
                self.website_data[website]['content'] = r.text
            else:
                print(f"Failed to access {website}")

    def get_header_tags(self):

        header_numbers = (1, 2, 3)

        for site in self.website_data:

            self.website_data[site]['headers'] = []

            soup = BeautifulSoup(self.website_data[site]['content'], "html.parser")

            for i in header_numbers:
                header_tags = list(soup.find_all(f'h{i}', text=True))

                for tag in header_tags:
                    self.website_data[site]['headers'].append(tag.string.strip())
