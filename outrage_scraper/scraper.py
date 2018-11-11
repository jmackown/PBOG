from bs4 import BeautifulSoup
import requests
import psycopg2
import ruamel.yaml as yaml
import spacy

nlp = spacy.load('en_core_web_sm')



class Scraper:

    def __init__(self):

        self.website_data = {}
        self.websites = set(["https://thelincolnite.co.uk/", ])
        self.angry_words = yaml.load(open('angry_words.yaml').read(), Loader=yaml.Loader)
        self.animals = yaml.load(open('animals.yaml').read(), Loader=yaml.Loader)
        self.ignore = yaml.load(open('ignore.yaml').read(), Loader=yaml.Loader)




    def update_urls(self):
        print("Updating URLS")
        conn = psycopg2.connect(dbname="outrage", user="postgres", host="outrage_db", port='5432')

        cur = conn.cursor()
        cur.execute("SELECT url FROM url_lists;")

        for row in cur.fetchall():
            url = row[0]

            if 'http://' not in url:
                url = 'http://' + url

            if url and url != '':
                self.websites.add(url)

        conn.close()

    def scrape(self):
        self.update_urls()
        self.get_content_in_sites()
        self.get_header_tags()

        conn = psycopg2.connect(dbname="outrage", user="postgres", host="outrage_db", port='5432')
        cur = conn.cursor()

        for site in self.website_data:
            for headline in self.website_data[site]['headers']:
                headline = headline.replace("'", "''")

                print(f"Inserting {headline} for {site}")

                outrage_rank = self.rank_words(headline)

                noun = self.find_noun(headline)

                sql = f"INSERT INTO scraped_data (headline, source, noun, scrape_time, outrage_rank) " \
                      f"SELECT '{headline}', '{site}', '{noun}', now(), '{outrage_rank}' " \
                      f"WHERE NOT EXISTS (SELECT 1 FROM scraped_data WHERE headline = '{headline}');"

                try:
                    cur.execute(sql)
                except psycopg2.ProgrammingError as e:
                    print(e)

        print("Commiting!")
        conn.commit()

        conn.close()

        return self.website_data

    def get_content_in_sites(self):
        print("Getting Content")

        for website in self.websites:

            self.website_data[website] = {}

            print(f"Getting content for {website}")

            try:
                r = requests.get(website)
            except:
                print(f"FAILED: {website}")

            if r.status_code == 200:
                self.website_data[website]['content'] = r.text
            else:
                del self.website_data[website]
                print(f"Failed to access {website}")

    def get_header_tags(self):
        print("Getting Headers")

        header_numbers = (1, 2, 3)

        for site in self.website_data:

            self.website_data[site]['headers'] = []

            soup = BeautifulSoup(self.website_data[site]['content'], "html.parser")

            for i in header_numbers:
                header_tags = list(soup.find_all(f'h{i}', text=True))

                for tag in header_tags:
                    self.website_data[site]['headers'].append(tag.string.strip())

    def rank_words(self, headline):
        score = 0
        words = headline.split()

        for word in words:
            if word in self.angry_words:
                score += 1

        for word in words:
            if word in self.animals:
                score += 2

        for word in words:
            if word in self.ignore:
                score = 0

        print(f"Ranking {headline} with score '{score}'")

        return score

    def find_noun(self, headline):


        doc = nlp(f'{headline}')

        for token in doc:
            if token.pos_ in ('NOUN'):
                return token

        print(f"Finding nouns in {headline}'")


