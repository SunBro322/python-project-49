import random


def logic_for_game():
    description_game = ('Answer "yes" if the number is even, '
                        'otherwise answer "no".')
    print(description_game)
    random_value = random.randint(1, 100)
    even_or = ''
    if random_value % 2 == 0:
        even_or = 'yes'
    else:
        even_or = 'no'
    print(f'Question: {random_value}')
    get_answer = str(input('Your answer: '))
    return get_answer, even_or
