import random

DESCRIPTION = ('Answer "yes" if the number is even, '
               'otherwise answer "no".')


def generate_round_data():
    random_value = random.randint(1, 100)
    result = ''
    if random_value % 2 == 0:
        result = 'yes'
    else:
        result = 'no'

    question_for_gamers = random_value
    return question_for_gamers, result
