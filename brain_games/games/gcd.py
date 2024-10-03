import random
import math


def performs_game():
    description_game = "Find the greatest common divisor of given numbers."
    result = 0
    first_value = random.randint(0, 100)
    second_value = random.randint(0, 100)
    result = math.gcd(first_value, second_value)
    question_for_gamers = f"Question: {first_value} {second_value}"

    return description_game, question_for_gamers, str(result)
