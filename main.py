from story_generators import *
from util import load_openai_api_key

if __name__ == '__main__':
    # Initialise OpenAi API Key (otherwise, generator is unusable)
    load_openai_api_key()
    response = children_story_generator(topics="Bee, Vampire")
    print(response)
