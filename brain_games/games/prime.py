import random
import math

DESCRIPTION = ('Answer "yes" if given number is prime. '
               'Otherwise answer "no".')


def is_prime(value):
    if value <= 1:
        return False
    number_sqrt = int(math.sqrt(value))
    divisors = range(2, (number_sqrt + 1))
    for element in divisors:
        if value % element == 0:
            return False
    return True


def generate_round_data():
    question_for_gamers = random.randint(1, 101)
    result = ''

    if is_prime(question_for_gamers):
        result = 'yes'
    else:
        result = 'no'

    return question_for_gamers, result
