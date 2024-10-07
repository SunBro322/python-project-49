import random
from brain_games import constant


def generate_round_data():
    DESCRIPTION = constant.DESCRIPTION_PROGRESSION
    array_of_values = []
    for i in range(1, 100):
        array_of_values.append(i)

    value_for_slice = 0
    invisible_value = 0

    step_value = random.randint(1, 5)
    if 1 <= step_value <= 2:
        value_for_slice = 10
    else:
        value_for_slice = 30

    start_value = random.randint(0, 20)
    finish_value = start_value + value_for_slice

    slice_of_values = array_of_values[start_value:finish_value:step_value]
    invisible_value = slice_of_values[random.randint(0,
                                                     len(slice_of_values) - 1)]
    slice_of_values[slice_of_values.index(invisible_value)] = '..'
    result = ' '.join(map(str, slice_of_values))

    question_for_gamers = result

    return DESCRIPTION, question_for_gamers, str(invisible_value)
