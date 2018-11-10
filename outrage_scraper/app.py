from bs4 import BeautifulSoup
import requests


class Scraper:

    def __init__(self):
        self.websites = ("https://thelincolnite.co.uk/",)
        self.content = {}

        self.get_content_in_sites()

        self.get_header_tags()

    def get_content_in_sites(self):

        for website in self.websites:

            r = requests.get(website)

            if r.status_code == 200:
                # print(r.content)
                self.content[website] = r.content
                # print(self.content[website])

            else:
                print(f"Failed to access {website}")

    def get_header_tags(self):


        with open('test.txt', 'wb') as file:
            file.write(self.content['https://thelincolnite.co.uk/'])
            file.close()

        print(len(self.content))

        for site in self.content:

            for content in self.content[site]:
                pass
                # print(content)

                # soup = BeautifulSoup(content, "html.parser")

                # for i in tag_numbers:
                #     print(soup.find(f'h{i}'))




scraper = Scraper()
