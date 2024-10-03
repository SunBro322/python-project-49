import random


def performs_game():
    description_game = ('Answer "yes" if given number is prime. '
                        'Otherwise answer "no".')
    print(description_game)
    result = ''
    value = random.randint(1, 101)
    print(f"Question: {value}")

    if value == (2 or 3 or 5 or 7):
        result = 'no'
    elif value > 3 and (value % 2 != 0
                        and value % 3 != 0
                        and value % 5 != 0
                        and value % 7 != 0):
        result = 'yes'
    else:
        result = 'no'

    user_response = str(input("Your answer: "))
    return user_response, str(result)
