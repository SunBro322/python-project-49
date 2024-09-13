#!/usr/bin/env python3
import random, math
from brain_games import cli


def hello():
    print("Welcome to the Brain Games!")


def nod(name):
    count_correct = 0
    print("Find the greatest common divisor of given numbers.")

    while count_correct < 3:
        result = 0
        first_value = random.randint(0, 100)
        second_value = random.randint(0, 100)
        result = math.gcd(first_value, second_value)
        print(f"Question: {first_value} {second_value}")
        get_answer = str(input("Your answer: "))

        if get_answer == str(result):
            print("Correct!")
            count_correct += 1
        else:
            print(f"{get_answer}' is wrong answer ;(. Correct answer was '{result}'. \nLet's try again, {name}!")
            break

        if count_correct == 3:
            print(f"Congratulations, {name}!")


def main():
    hello()
    name = cli.welcome_user()
    nod(name)


if __name__ == 'main':
    main()
