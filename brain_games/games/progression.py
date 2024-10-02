import random


def logic_for_game():
    description_game = "What number is missing in the progression?"
    print(description_game)
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

    return get_answer, str(get_value)
