import re


def try_except(text: str) -> float | None:
    while True:
        try:
            a = float(input(text))
            if a <= 0:
                raise ValueError

            return a
        except Exception as e:
            print("Некорректный ввод")


print("Калькулятор ИМТ")
print("""
1. Вес в кг
2. Вес в фунтах
""")

choice_w = input("Ваш выбор: ").strip()

while choice_w not in ("1", "2"):
    print("Некорректный выбор")
    choice_w = input("Ваш выбор: ").strip()

print("""
1. Рост в см
2. Рост в футах (в формате f'i")
""")
choice_h = input("Ваш выбор: ").strip()

while choice_h not in ("1", "2"):
    print("Некорректный выбор")
    choice_h = input("Ваш выбор: ").strip()

weight = try_except("Введите ваш вес: ")

if choice_h == "1":
    height = try_except("Введите ваш рост в см: ")
else:
    height = input("Введите ваш рост (f'i\"): ")
    while not re.fullmatch("[1-9]+\\.?\\d*'\\d+\\.?\\d*\"?", height):
        print("Некорректный ввод")
        height = input("Введите ваш рост (f'i\"): ")
    f, i = map(float, height.strip('"').split("'"))
    height = (f * 12 + i) * 2.54

if choice_w == "2":
    weight /= 2.20462

IMT = weight / ((height / 100) ** 2)
if IMT < 16:
    res = "У вас выраженный дефицит массы тела"
elif 16 <= IMT < 18.5:
    res = "У вас недостаточный вес"
elif 18.5 <= IMT <= 25:
    res = "Ваш вес в норме"
elif 25 <= IMT <= 30:
    res = "У вас избыточная масса тела"
elif 30 <= IMT <= 35:
    res = "У вас ожирение I степени"
elif 35 <= IMT <= 40:
    res = "У вас ожирение II степени"
else:
    res = "У вас ожирение III степени (морбидное)"


print()
print(f"Ваш ИМТ: {IMT:.1f}")
print(res)
