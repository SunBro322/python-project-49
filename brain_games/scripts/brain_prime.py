#!/usr/bin/env python3
import random
from brain_games import cli


def hello():
    print("Welcome to the Brain Games!")


def simple_val_or_not(name):
    count_correct = 0
    simple_or_not = ''

    print('Answer "yes" if given number is prime. '
          'Otherwise answer "no".')
    while count_correct < 3:
        value = random.randint(1, 101)

        if value > 3 and (value % 2 != 0 and value % 3 != 0
                          and value % 5 != 0
                          and value % 7 != 0):
            simple_or_not = 'yes'
        else:
            simple_or_not = 'no'
        print(f"Question: {value}")
        get_answer = str(input("Your answer: "))
        if get_answer == simple_or_not:
            print("Correct!")
            count_correct += 1
        else:
            print(f"'{get_answer}' is wrong answer ;(. "
                  f"Correct answer was '{simple_or_not}'.")
            print(f"Let's try again, {name}!")
            break

        if count_correct == 3:
            print(f"Congratulations, {name}!")


def main():
    hello()
    name = cli.welcome_user()
    simple_val_or_not(name)


if __name__ == 'main':
    main()
