import openai
import nltk


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


def children_story_generator(topics):
    train_ex = {
        'topics': "Dog, Knight, Dragon",
        'num_sentences': "Ten",
        'story': "There was once a valiant knight who loved nothing more than to protect the innocent. One day, as he was out on a walk, he came across a poor dog that had been injured. The knight picked up the dog and took it back to his home, where he tended to its wounds and gave it some food. The knight named the dog Sir Lancelot and taught it how to fight like a knight. One day, while Sir Lancelot was out patrolling the kingdom, he heard a noise coming from a nearby tower. He approached the tower and saw that it was being guarded by a huge dragon! Sir Lancelot bravely fought the dragon and defeated it, rescuing the princess inside. The people of the kingdom were so grateful to Sir Lancelot for his bravery that they made him their new king."
    }
    prompt = f"Topic: {train_ex['topics']}\n" + \
             f"{train_ex['num_sentences']} Sentence Children Story: " + \
             f"{train_ex['story']}\n" + \
             f"Topic: {topics}\n" + \
             "One Hundred Sentence Children Story: "

    return openai.Completion.create(
        engine="text-davinci-001",
        prompt=prompt,
        temperature=0.8,
        max_tokens=2_048 - 300,
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
