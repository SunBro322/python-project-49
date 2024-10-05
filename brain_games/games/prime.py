import random


def generate_round_data():
    DESCRIPTION = ('Answer "yes" if given number is prime. '
                   'Otherwise answer "no".')
    result = ''
    value = random.randint(1, 101)
    question_for_gamers = value

    def is_prime():
        if value == (2 or 3 or 5 or 7):
            return False
        elif value > 3 and (value % 2 != 0
                            and value % 3 != 0
                            and value % 5 != 0
                            and value % 7 != 0):
            return True
        else:
            return False

    if is_prime():
        result = 'yes'
    else:
        result = 'no'

    return DESCRIPTION, question_for_gamers, result
