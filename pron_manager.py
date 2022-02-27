from nltk.stem import PorterStemmer

class PronounManager:
    def __init__(self):
        self.pron_noun_dict = dict()
        self.noun_pron_dict = {
            "prince": "he",
            "knight": "he",
            "king": "he",
            "princess": "she",
            "emili": "she",
            "queen": "she",
            "witch": "she",
            "dragon": "it/he",
            "dog": "it/he",
            "cat": "it/she",
            "duck": "it",
            "vampire": "she/it",
        }
        self.simpler_noun = {
            "he": "he",
            "him": "he",
            "his": "he",
            "she": "she",
            "her": "she",
            "hers": "she",
            "it": "it",
            "its": "it",
        }
        self.ps = PorterStemmer()

    def add(self, noun):
        noun = noun.lower()
        noun = self.ps.stem(noun)
        if noun in self.noun_pron_dict.keys():
            self.pron_noun_dict[self.noun_pron_dict[noun]] = noun

    def get(self, pron):
        pron = pron.lower()
        if pron not in self.simpler_noun.keys():
            return 'NOTHING'
        pron = self.simpler_noun[pron]
        pron_noun_tup_list = [(key, value) for (key, value) in
                              self.pron_noun_dict.items() if pron in key]
        pron_noun_tup_list.sort(key=lambda y: len(y[0]))
        if len(pron_noun_tup_list) != 0:
            return pron_noun_tup_list[0][1]
        return 'NOTHING'

    def print(self):
        print(self.pron_noun_dict)

