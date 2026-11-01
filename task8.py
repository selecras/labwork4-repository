# ВАРИАНТ 8


def prime_divisors(num: int) -> list[int]:
    temp = 2
    lst = []

    while temp * temp <= num:
        if num % temp == 0:
            lst.append(temp)
            while num % temp == 0:
                num //= temp
        temp += 1

    if num > 1 and lst:
        lst.append(num)
    return lst


while True:
    try:
        number = int(input("Введите целое число (-1 для выхода): "))
    except ValueError:
        print("Некорректный ввод")
        continue

    if number == -1:
        break

    if number <= 1:
        print("Введите число больше единицы")
        continue

    lst = prime_divisors(number)
    if not lst:
        print(f"Число {number} -- простое\n")
    else:
        print(f"Число {number} -- составное\nСписок простых делителей:", end=" ")
        print(*lst, sep=", ", end="\n\n")
