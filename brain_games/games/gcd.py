import random
import math
from brain_games import constant


def generate_round_data():
    DESCRIPTION = constant.DESCRIPTION_GCD
    result = 0
    first_value = random.randint(0, 100)
    second_value = random.randint(0, 100)
    result = math.gcd(first_value, second_value)
    question_for_gamers = f"{first_value} {second_value}"

    return DESCRIPTION, question_for_gamers, str(result)
