#!/usr/bin/env python3
import random
from brain_games import cli
def hello():
    print("Welcome to the Brain Games!")

def calc(name):
    count_correct = 0

    print("What is the result of the expression?")
    while count_correct < 3:
        result = 0
        match_symbol = ['+', '-', '*']
        random_symbol_for_task = match_symbol[random.randint(0, 2)]
        first_value = random.randint(0, 100)
        second_value = random.randint(0, 100)

        if random_symbol_for_task == '+':
            print(f"Question: {first_value} + {second_value}")
            result = first_value + second_value
        elif random_symbol_for_task == '-':
            print(f"Question: {first_value} - {second_value}")
            result = first_value - second_value
        elif random_symbol_for_task == '*':
            print(f"Question: {first_value} * {second_value}")
            result = first_value * second_value

        get_answer = str(input("Your answer: "))
        if get_answer == str(result):
            print("Correct!")
            count_correct += 1
        else:
            print(f"{get_answer}' is wrong answer ;(. Correct answer was '{result}'. \nLet's try again, {name}!")
            break



def main():
    hello()
    name = cli.welcome_user()
    calc(name)


if __name__ == 'main':
    main()