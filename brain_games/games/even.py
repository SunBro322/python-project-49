import random


def performs_game():
    description_game = ('Answer "yes" if the number is even, '
                        'otherwise answer "no".')
    print(description_game)
    random_value = random.randint(1, 100)
    result = ''
    if random_value % 2 == 0:
        result = 'yes'
    else:
        result = 'no'
    print(f'Question: {random_value}')
    user_response = str(input('Your answer: '))
    return user_response, result
