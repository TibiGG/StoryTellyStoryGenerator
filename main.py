import os
from dotenv import load_dotenv

from story_generators import *


def load_openai_api_key():
    load_dotenv()
    openai.api_key = os.getenv('OPENAI_API_KEY')


if __name__ == '__main__':
    load_openai_api_key()

    response = children_story_generator()
    print(response)
