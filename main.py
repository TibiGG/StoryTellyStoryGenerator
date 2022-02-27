from pos_extractor import PosExtractor
from story_generators import *
from util import load_openai_api_key
import settings
import re

if __name__ == '__main__':
    # Initialise OpenAi API Key (otherwise, generator is unusable)
    load_openai_api_key()
    if settings.should_generate_new_story:
        response = children_story_generator(topics="Bee, Vampire")
    else:
        response = "Emily loved knights. Her favorite was Sir Lancelot. One day she found a dog with a broken leg on the side of the road. She took it home and nursed it back to health. She named him Sir Lancelot and taught him how to be a knight. One night, when Emily was asleep, Sir Lancelot woke her up. There was a vampire in her room! Sir Lancelot bravely fought the vampire and saved Emily's life."

    response_sentences = re.split("[.!?]\s", response)
    print(response_sentences)
    # substantives, verbs, adjectives = \
    nouns, verbs = PosExtractor().extract_from_sentence(response_sentences[0])
    print(nouns)
    print(verbs)
