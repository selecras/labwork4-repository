# Делится ли число num на число divisor
def divisible(num: int, divisor: int | float) -> bool:
    if num % divisor == 0:
        return True
    return False


# Ввод чисел
number = int(input("Введите число: "))
divisor = int(input("Введите делитель: "))

# Проверка
if divisible(number, divisor):
    print(f"Число {number} делится на {divisor}")
else:
    print(f"Число {number} не делится на {divisor}")
