# Паттерн для скриптов
import prompt


def run(game):
    how_many_try = 3
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    description, _, _ = game.generate_round_data()
    print(description)
    for i in range(how_many_try):
        _, question, result = game.generate_round_data()
        print(f"Question: {question}")
        answer = str(input("Your answer: "))
        if answer == result:
            print("Correct!")
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{result}'.")
            print(f"Let's try again, {name}!")
            break
    else:
        print(f"Congratulations, {name}!")
