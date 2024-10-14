import random

DESCRIPTION = ("What number is missing in the "
               "progression?")


def generate_round_data():
    generate_round_data.DESCRIPTION = DESCRIPTION
    start = 1
    end = 100
    step = 4
    progression = list(range(start, end + 1, step))
    random_index = random.randint(start, len(progression))
    invisible_value = progression[random_index]
    progression[random_index] = ".."
    result = ' '.join(map(str, progression))
    question_for_gamers = result

    return question_for_gamers, str(invisible_value)
