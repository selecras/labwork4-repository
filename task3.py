# Ввод возраста
age = int(input("Введите возраст: "))

if age < 0:
    print("Некорректный возраст")
if age <= 12:
    print("Ребёнок")
if age <= 17:
    print("Подросток")
if age <= 64:
    print("Взрослый")
else:
    print("Пожилой")
