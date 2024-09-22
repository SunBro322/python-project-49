#!/usr/bin/env python3
import random
import math
from brain_games import cli
from brain_games import pattern_for_games


def hello():
    print("Welcome to the Brain Games!")


def nod(name):
    print("Find the greatest common divisor of given numbers.")

    def gcd():
        result = 0
        first_value = random.randint(0, 100)
        second_value = random.randint(0, 100)
        result = math.gcd(first_value, second_value)
        print(f"Question: {first_value} {second_value}")
        get_answer = str(input("Your answer: "))

        return get_answer, str(result)

    pattern_for_games.pattern(gcd, name)


def main():
    hello()
    name = cli.welcome_user()
    nod(name)


if __name__ == 'main':
    main()
