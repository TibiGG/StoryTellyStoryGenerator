import openai


def horror_story_generator():
    return openai.Completion.create(
        engine="text-davinci-001",
        prompt="Topic: Breakfast\nTwo-Sentence Horror Story: He always stops crying when I pour the milk on his cereal. I just have to remember not to let him see his face on the carton.\n    \nTopic: Wind\nTwo-Sentence Horror Story:",
        temperature=0.8,
        max_tokens=60,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0
    )


def children_story_generator():
    return openai.Completion.create(
        engine="text-davinci-001",
        prompt="Topic: Knight, Princess, Dragon\n"
               "Three Sentence Children Story: Once upon a time, there was a honorable knight. He was tasked to save a princess from a tower. But this tower was guarded by a fiersome dragon.\n"
               "\n"
               "Topic: Dog, Vampire, Tower\n"
               "Ten Sentence Children Story:",
        temperature=0.8,
        max_tokens=2_048 - 200,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0
    )

def continue_story(story):
    return openai.Completion.create(
        engine="text-davinci-001",
        prompt=story,
        temperature=0.8,
        max_tokens=2_048 - 234,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0
    )
