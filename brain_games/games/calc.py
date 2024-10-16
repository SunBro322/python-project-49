import random

DESCRIPTION = "What is the result of the expression?"


def generate_round_data():
    result = 0
    suitable_symbol = ['+', '-', '*']
    random_suitable_symbol = suitable_symbol[random.randint(0, 2)]
    first_value = random.randint(0, 100)
    second_value = random.randint(0, 100)
    question_for_gamers = (f"{first_value} {random_suitable_symbol} "
                           f"{second_value}")

    if random_suitable_symbol == '+':
        result = first_value + second_value
    elif random_suitable_symbol == '-':
        result = first_value - second_value
    elif random_suitable_symbol == '*':
        result = first_value * second_value

    return question_for_gamers, str(result)
