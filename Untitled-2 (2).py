class program:
    a = int(input("Введите сумму: "))
    b = int(input("Введите оклад: "))
    s = str(input("Введите имя: "))
    if a > 0:
        v = int(a / 100 * 5)
        c = v + b
        print(f"{s} give {c}")