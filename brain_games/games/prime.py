import random


def is_prime():
    print('Answer "yes" if given number is prime. '
          'Otherwise answer "no".')
    simple_or_not = ''
    value = random.randint(1, 101)
    print(f"Question: {value}")

    if value == (2 or 3 or 5 or 7):
        simple_or_not = 'no'
    elif value > 3 and (value % 2 != 0
                        and value % 3 != 0
                        and value % 5 != 0
                        and value % 7 != 0):
        simple_or_not = 'yes'
    else:
        simple_or_not = 'no'

    get_answer = str(input("Your answer: "))
    return get_answer, str(simple_or_not)
