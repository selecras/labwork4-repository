while True:
    try:
        x, y = map(float, input("Введите координаты точки через пробел: ").split())
        break
    except Exception:
        print("Некорректный ввод")

flag = None
if x > 0:
    if y > 0:
        flag = "в первой четверти"
    elif y < 0:
        flag = "в четвертой четверти"
    else:
        flag = "на оси OX"
elif x < 0:
    if y > 0:
        flag = "во второй четверти"
    elif y < 0:
        flag = "в третьей четверти"
    else:
        flag = "на оси OX"
else:
    if y == 0:
        flag = "в начале координат"
    else:
        flag = "на оси OY"

print(f"Точка ({x}, {y}) находится {flag}.")
