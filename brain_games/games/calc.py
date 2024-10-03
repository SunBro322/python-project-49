import random


def performs_game():
    description_game = "What is the result of the expression?"
    print(description_game)
    result = 0
    suitable_symbol = ['+', '-', '*']
    random_suitable_symbol = suitable_symbol[random.randint(0, 2)]
    first_value = random.randint(0, 100)
    second_value = random.randint(0, 100)
    question_for_gamers = (f"Question: {first_value} {random_suitable_symbol} "
                           f"{second_value}")

    if random_suitable_symbol == '+':
        print(question_for_gamers)
        result = first_value + second_value
    elif random_suitable_symbol == '-':
        print(question_for_gamers)
        result = first_value - second_value
    else:
        print(question_for_gamers)
        result = first_value * second_value

    user_response = str(input("Your answer: "))
    return user_response, str(result)
