import re
import ruamel.yaml as yaml
import spacy

nlp = spacy.load('en_core_web_sm')

class Outragify:

    def __init__(self):
        self.angry_words = yaml.load(open('angry_words.yaml').read(), Loader=yaml.Loader)
        self.happy_words = yaml.load(open('happy_words.yaml').read(), Loader=yaml.Loader)
        self.animal_words = yaml.load(open('animals.yaml').read(), Loader=yaml.Loader)
        self.outrage_words = yaml.load(open('outrage_words.yaml').read(), Loader=yaml.Loader)

    def rank_words(self, headline):
        score = 0
        rank = 0

        headline = re.sub(r'[^\w\s]', '', headline).lower()

        words = headline.split()

        if len(words) > 2:

            for word in words:
                if word in self.angry_words:
                    score += 1
                if word in self.happy_words:
                    score -= 1
                if word in self.animal_words:
                    score += 1
                if word in self.outrage_words:
                    score += 1

            rank = (score / 4) / len(words)

            print(f"Ranking {headline} with score '{score}'")

        return score, rank

    def find_noun(self, headline):
        doc = nlp(f'{headline}')

        for token in doc:
            if token.pos_ in ('NOUN'):
                return token

        print(f"Finding nouns in {headline}'")
