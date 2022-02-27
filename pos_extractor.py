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
        all_imp_stuff = []
        sbjs = []
        objs = []
        verbs = []
        prons = []
        for entity in flair_sentence.get_spans('pos'):
            pos_labels = entity.to_dict()['labels']
            token_text = entity.to_dict()['text']
            for label in pos_labels:
                if label.value in 'PROPN':
                    sbjs.append(token_text)
                    all_imp_stuff.append(token_text)
                    break
                elif label.value in 'NOUN':
                    objs.append(token_text)
                    all_imp_stuff.append(token_text)
                    break
                elif label.value in 'VERB':
                    verbs.append(token_text)
                    all_imp_stuff.append(token_text)
                    break
                elif label.value in 'PRON':
                    prons.append(token_text)
                    all_imp_stuff.append(token_text)
                    break

        return sbjs, objs, verbs, prons, all_imp_stuff
