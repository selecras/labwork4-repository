from time import sleep
import random


def random_num() -> int:
    sleep(0.5)
    print("Происходит загадывание числа...")
    sleep(1)
    to_guess = random.randint(1, 100)
    print("Число загадано!")
    return to_guess


previous_games = []
print("Угадайка чисел")
print("Компьютер загадает число от 1 до 100, а ваша задача -- угадать число.")
to_guess = random_num()
tries = []

while True:
    try:
        num = int(input("Введите число: "))
    except ValueError:
        print("Некорректный ввод")
        continue
    tries.append(num)
    if to_guess < num:
        print(f"Загаданное число меньше, чем {num}\n")
    elif to_guess > num:
        print(f"Загаданное число больше, чем {num}\n")
    else:
        previous_games.append((to_guess, tries.copy()))
        print(f"Верно! Вы угадали число {to_guess}!\nКоличество попыток: {len(tries)}.")
        prev_ans = input("Хотите посмотреть предыдущие игры? (y/n): ").lower()
        while prev_ans not in ("y", "n"):
            print("Некорректный ввод")
            prev_ans = input("Хотите посмотреть предыдущие игры? (y/n): ")
        if prev_ans == "y":
            for i, (num_, attempts) in enumerate(previous_games, 1):
                print(f"{i}) Загаданное число: {num_}")
                print(f"Количество затраченных попыток: {len(attempts)}")
                for j, attempt in enumerate(attempts, 1):
                    print(f"Попытка {j}) {attempt}")
                print()

        ans = input("Попробовать снова? (y/n): ").lower()
        while ans not in ("y", "n"):
            print("Некорректный ввод")
            ans = input("Попробовать снова? (y/n): ")
        if ans == "y":
            tries = []
            print("Начинаем снова")
            to_guess = random_num()
        else:
            break
