import random
from brain_games import constant


def is_prime(value):
    if value == (2 or 3 or 5 or 7):
        return False
    elif value > 3 and (value % 2 != 0
                        and value % 3 != 0
                        and value % 5 != 0
                        and value % 7 != 0):
        return True
    else:
        return False


def generate_round_data():
    value = random.randint(1, 101)
    question_for_gamers = value
    DESCRIPTION = constant.DESCRIPTION_PRIME
    result = ''

    if is_prime(value):
        result = 'yes'
    else:
        result = 'no'

    return DESCRIPTION, question_for_gamers, result
