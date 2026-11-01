a = float(input("Введите сторону a: "))
b = float(input("Введите сторону b: "))
c = float(input("Введите сторону c: "))

if a + b > c and a + c > b and b + c > a:
    flag = ""
    if a**2 + b**2 + c**2 == 2 * max(a, b, c) ** 2:
        flag = " прямоугольный"
    if a == b == c:
        print("Равносторонний треугольник")
    elif a == b or a == c or b == c:
        print(f"Равнобедренный{flag} треугольник")
    else:
        print(f"Разносторонний{flag} треугольник")
else:
    print("Треугольник не существует")
