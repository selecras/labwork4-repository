# Делится ли число num на число divisor
def divisible(num: int, divisor: int | float) -> bool:
    if num % divisor == 0:
        return True
    return False


def negative_positive(num: int | float) -> str:
    if num > 0:
        return "положительное"
    elif num < 0:
        return "отрицательное"
    return "ноль"


# Ввод чисел с проверкой на корректность
while True:
    try:
        number = int(input("Введите число: "))
        divisor = float(input("Введите делитель: "))
        break
    except Exception as e:
        print("Некорректный ввод")

# Условие
if divisible(number, divisor):
    print(f"Число {number} делится на {divisor}")
else:
    print(f"Число {number} не делится на {divisor}")
print(f"{number} -- {negative_positive(number)}")
