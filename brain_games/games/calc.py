import random


def calculate():
    description_game = "What is the result of the expression?"
    print(description_game)
    result = 0
    match_symbol = ['+', '-', '*']
    random_symbol_for_task = match_symbol[random.randint(0, 2)]
    first_value = random.randint(0, 100)
    second_value = random.randint(0, 100)
    question_for_gamers = f"Question: {first_value} {random_symbol_for_task} {second_value}"

    if random_symbol_for_task == '+':
        print(question_for_gamers)
        result = first_value + second_value
    elif random_symbol_for_task == '-':
        print(question_for_gamers)
        result = first_value - second_value
    else:
        print(question_for_gamers)
        result = first_value * second_value

    get_answer = str(input("Your answer: "))
    return get_answer, str(result)
