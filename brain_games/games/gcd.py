import random
import math

DESCRIPTION = "Find the greatest common divisor of given numbers."


def generate_round_data():
    generate_round_data.DESCRIPTION = DESCRIPTION
    result = 0
    first_value = random.randint(0, 100)
    second_value = random.randint(0, 100)
    result = math.gcd(first_value, second_value)
    question_for_gamers = f"{first_value} {second_value}"

    return question_for_gamers, str(result)
