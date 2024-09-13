#!/usr/bin/env python3
import random
from brain_games import cli


def hello():
    print("Welcome to the Brain Games!")


def even_or_not(name):
    count_correct = 0
    print("Answer 'yes' if the number is even, otherwise answer 'no'.")

    while count_correct < 3:
        random_value = random.randint(1, 100)
        print(f'Question: {random_value}')
        get_answer = str(input('Your answer: '))
        if get_answer == 'yes':
            if random_value % 2 == 0:
                count_correct += 1
                print('Correct')
            else:
                print("'yes' is wrong answer ;(. Correct answer was 'no'")
                break
        elif get_answer == 'no':
            if random_value % 2 != 0:
                count_correct += 1
                print('Correct')
            else:
                print("'no' is wrong answer ;(. Correct answer was 'yes'")
                break
        else:
            print("Is not correct answer ;(")
            break

    if count_correct == 3:
        print(f"Congratulations, {name}!")


def main():
    hello()
    name = cli.welcome_user()
    even_or_not(name)


if __name__ == 'main':
    main()
