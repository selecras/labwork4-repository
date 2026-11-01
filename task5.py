a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
operation = input("Введите операцию (+, -, *, /, //): ").strip()

match operation:
    case "+":
        print(f"Результат: {a + b}")
    case "-":
        print(f"Результат: {a - b}")
    case "*":
        print(f"Результат: {a * b}")
    case "/":
        try:
            print(f"Результат: {a / b}")
        except ZeroDivisionError:
            print("Деление на ноль невозможно")
    case "//":
        try:
            print(f"Результат: {a // b}")
        except ZeroDivisionError:
            print("Деление на ноль невозможно")
    case _:
        print("Неизвестная операция")
