# Паттерн для скриптов
import prompt


def pattern(func):
    how_many_try = 3
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    for i in range(how_many_try):
        answer, result = func.logic_for_game()
        if answer == result:
            print("Correct!")
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{result}'.")
            print(f"Let's try again, {name}!")
            break
    else:
        print(f"Congratulations, {name}!")
