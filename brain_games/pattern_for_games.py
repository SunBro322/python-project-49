# Паттерн для скриптов
def pattern(func, name):
    counter = 0
    while counter < 3:
        a = func()
        if a[0] == a[1]:
            print("Correct!")
            counter += 1
        else:
            print(f"'{a[0]}' is wrong answer ;(. "
                  f"Correct answer was '{a[1]}'.")
            print(f"Let's try again, {name}!")
            break
    if counter == 3:
        print(f"Congratulations, {name}!")
