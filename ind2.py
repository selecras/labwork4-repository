def convert(num: int | float, base: int, accuracy: int = 0):
    result = ""
    if num == 0:
        return "0"
    if int(num) == 0:
        result = "0"
    alp = "0123456789" + "".join(sorted("qwertyuiopasdfghjklzxcvbnm".upper()))
    flag = 1

    if int(num) == num:
        flag = 0

    temp = int(num)

    while temp > 0:
        result += alp[temp % base]
        temp //= base

    result = result[::-1]

    if flag and accuracy != 0:
        result += "."
        temp = num - int(num)
        for _ in range(accuracy):
            temp *= base
            result += alp[int(temp)]
            temp = temp - int(temp)

    return result.strip("0") if "." in result else result


print("Перевод в 2-ую, 8-ую и 16-ую системы счисления")
print("""1. Из 10-ой в 2-ую
2. Из 10-ой в 8-ую
3. Из 10 в 16-ую
4. Выход
""")
while 1:
    choice = input("Ваш выбор: ")
    while choice not in ("1", "2", "3", "4"):
        print("Некорректный выбор")
        choice = input("Ваш выбор: ")

    if choice == "4":
        break

    while 1:
        try:
            num = float(input("Введите число в 10-ой: "))
            break
        except Exception:
            print("Некорректный ввод")

    acc = 0
    if num != int(num):
        while 1:
            try:
                acc = int(input("Введите желаемую точность (0-16): "))
                if not (16 >= acc >= 0):
                    raise ValueError
                break
            except Exception:
                print("Некорректный ввод")

    res = convert(num, (2, 8, 16)[int(choice) - 1], acc)
    print(f"\n\n{num}(10) = {res}({(2, 8, 16)[int(choice) - 1]})\n\n")
