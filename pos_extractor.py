from flair.data import Sentence, Label
from flair.models import SequenceTagger


# Part of Sentence Extractor
class PosExtractor:
    def __init__(self):
        self.tagger = SequenceTagger.load("flair/upos-english-fast")

    def extract_from_sentence(self, flair_sentence):
        flair_sentence = Sentence(flair_sentence)
        self.tagger.predict(flair_sentence)

        print(flair_sentence)
        nouns = []
        verbs = []
        for entity in flair_sentence.get_spans('pos'):
            pos_labels = entity.to_dict()['labels']
            for label in pos_labels:
                if label.value in ['NOUN', 'PRON', 'PROPN']:
                    nouns.append(entity.to_dict()['text'])
                elif label.value in 'VERB':
                    verbs.append(entity.to_dict()['text'])

        return nouns, verbs

