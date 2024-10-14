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
    value = random.randint(1, 101)
    question_for_gamers = value
    generate_round_data.DESCRIPTION = DESCRIPTION
    result = ''

    if is_prime(value):
        result = 'yes'
    else:
        result = 'no'

    return question_for_gamers, result
