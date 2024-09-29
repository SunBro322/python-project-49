import random


def calculate():
    print("What is the result of the expression?")
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
    else:
        print(f"Question: {first_value} * {second_value}")
        result = first_value * second_value

    get_answer = str(input("Your answer: "))
    return get_answer, str(result)
