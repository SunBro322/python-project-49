#!/usr/bin/env python3
import random
from brain_games import cli


def hello():
    print("Welcome to the Brain Games!")


def even_or_not(name):
    count_correct = 0
    print('Answer "yes" if the number is even, '
          'otherwise answer "no".')

    while count_correct < 3:
        random_value = random.randint(1, 100)
        even_or = ''

        if random_value % 2 == 0:
            even_or = 'yes'
        else:
            even_or = 'no'

        print(f'Question: {random_value}')
        get_answer = str(input('Your answer: '))

        if get_answer == even_or:
            print("Correct!")
            count_correct += 1
        else:
            print(f"'{get_answer}' is wrong answer ;(. "
                  f"Correct answer was '{even_or}'.")
            print(f"Let's try again, {name}!")
            break

    if count_correct == 3:
        print(f"Congratulations, {name}!")


def main():
    hello()
    name = cli.welcome_user()
    even_or_not(name)


if __name__ == 'main':
    main()
