#!/usr/bin/env python3
import random
from brain_games import cli


def hello():
    print("Welcome to the Brain Games!")


def progression(name):
    count_correct = 0

    print("What number is missing in the progression?")
    while count_correct < 3:
        prog_result = []
        for i in range(1, 100):
            prog_result.append(i)

        compare_val = 0
        get_value = 0

        step_value = random.randint(1, 5)
        if 1 <= step_value <= 2:
            compare_val = 10
        else:
            compare_val = 30

        start_value = random.randint(0, 20)
        finish_value = start_value + compare_val

        str_result = prog_result[start_value:finish_value:step_value]
        get_value = str_result[random.randint(0, len(str_result) - 1)]
        str_result[str_result.index(get_value)] = '..'
        str_result = ' '.join(map(str, str_result))

        print(f"Question: {str_result}")

        get_answer = str(input("Your answer: "))
        if get_answer == str(get_value):
            print("Correct!")
            count_correct += 1
        else:
            print(f"'{get_answer}' is wrong answer ;(. "
                  f"Correct answer was '{get_value}'.")
            print(f"Let's try again, {name}!")
            break

    if count_correct == 3:
        print(f"Congratulations, {name}!")


def main():
    hello()
    name = cli.welcome_user()
    progression(name)


if __name__ == 'main':
    main()
