from bs4 import BeautifulSoup
import requests


class Scraper:

    def __init__(self):
        self.websites = ("https://thelincolnite.co.uk/",)
        self.website_data = {}

    def scrape(self):
        self.get_content_in_sites()
        self.get_header_tags()

        print("Scraping!")

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
