import random


def performs_game():
    description_game = ('Answer "yes" if the number is even, '
                        'otherwise answer "no".')
    random_value = random.randint(1, 100)
    result = ''
    if random_value % 2 == 0:
        result = 'yes'
    else:
        result = 'no'

    question_for_gamers = f'Question: {random_value}'
    return description_game, question_for_gamers, result
