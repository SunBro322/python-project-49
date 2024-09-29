# Паттерн для скриптов
def pattern(func, name):
    for i in range(3):
        a = func()
        if a[0] == a[1]:
            print("Correct!")
        else:
            print(f"'{a[0]}' is wrong answer ;(. "
                  f"Correct answer was '{a[1]}'.")
            print(f"Let's try again, {name}!")
            break
    else:
        print(f"Congratulations, {name}!")

