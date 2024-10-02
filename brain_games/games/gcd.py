import random
import math


def gcd():
    description_game = "Find the greatest common divisor of given numbers."
    print(description_game)
    result = 0
    first_value = random.randint(0, 100)
    second_value = random.randint(0, 100)
    result = math.gcd(first_value, second_value)
    print(f"Question: {first_value} {second_value}")
    get_answer = str(input("Your answer: "))

    return get_answer, str(result)
