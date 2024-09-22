#!/usr/bin/env python3
import random
from brain_games import cli
from brain_games import pattern_for_games


def hello():
    print("Welcome to the Brain Games!")


def even_or_not(name):
    print('Answer "yes" if the number is even, '
          'otherwise answer "no".')

    def even():
        random_value = random.randint(1, 100)
        even_or = ''
        if random_value % 2 == 0:
            even_or = 'yes'
        else:
            even_or = 'no'
        print(f'Question: {random_value}')
        get_answer = str(input('Your answer: '))
        return get_answer, even_or

    pattern_for_games.pattern(even, name)


def main():
    hello()
    name = cli.welcome_user()
    even_or_not(name)


if __name__ == 'main':
    main()
