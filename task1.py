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


# Ввод чисел
number = int(input("Введите число: "))
divisor = int(input("Введите делитель: "))

# Проверка
if divisible(number, divisor):
    print(f"Число {number} делится на {divisor}")
else:
    print(f"Число {number} не делится на {divisor}")
print(f"{number} -- {negative_positive(number)}")