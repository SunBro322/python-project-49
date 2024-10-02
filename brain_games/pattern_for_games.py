# Паттерн для скриптов
import prompt


def pattern(func):
    how_many_try = 3
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    for i in range(how_many_try):
        a = func()
        if a[0] == a[1]:
            print("Correct!")
        else:
            print(f"'{a[0]}' is wrong answer ;(. "
                  f"Correct answer was '{a[1]}'.")
            print(f"Let's try again, {name}!")
            break
    else:
        print(f"Congratulations, {name}!")
