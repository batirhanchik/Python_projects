a = int(input("Введите число: "))
b = int(input("Введите число: "))
c = int(input("Введите число: "))
x = int(input("Введите число: "))
y = int(input("Введите число: "))



if a * b < x * y:
    print("өтеді")
if a * c < x * y:
    print("өтеді")
if c * b < x * y:
    print("өтеді")
if b * a < x * y:
    print("өтеді")
else:
    print("өтпейді")