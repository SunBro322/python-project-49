import random
from brain_games import constant


def generate_round_data():
    generate_round_data.DESCRIPTION = constant.DESCRIPTION_EVEN
    random_value = random.randint(1, 100)
    result = ''
    if random_value % 2 == 0:
        result = 'yes'
    else:
        result = 'no'

    question_for_gamers = random_value
    return question_for_gamers, result
