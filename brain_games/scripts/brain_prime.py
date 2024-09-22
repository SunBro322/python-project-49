#!/usr/bin/env python3
import random
from brain_games import cli
from brain_games import pattern_for_games


def hello():
    print("Welcome to the Brain Games!")


def simple_val_or_not(name):
    print('Answer "yes" if given number is prime. '
          'Otherwise answer "no".')

    def is_prime():
        simple_or_not = ''
        value = random.randint(1, 101)
        print(f"Question: {value}")

        if value > 3 and (value % 2 != 0
                          and value % 3 != 0
                          and value % 5 != 0
                          and value % 7 != 0):
            simple_or_not = 'yes'
        else:
            simple_or_not = 'no'

        get_answer = str(input("Your answer: "))
        return get_answer, str(simple_or_not)

    pattern_for_games.pattern(is_prime, name)


def main():
    hello()
    name = cli.welcome_user()
    simple_val_or_not(name)


if __name__ == 'main':
    main()
