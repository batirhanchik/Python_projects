x = int(input("Введите число: "))
y = int(input("Введите число: "))
z = int(input("Введите число: "))

if x > 0:
    print("x: ", x ** 2)
    if y > 0:
        print("y: ", y ** 2)
        if z > 0:
            print("z: ", z ** 2)
elif y > 0:
    print("y: ", y ** 2)
elif z > 0:
    print("z: ", z ** 2)
else:
    print("sorry")