import math

x = float(input("x: "))
y = float(input("y: "))
z = float(input("z: "))

a = y + x / y ** 2 + abs(x**2/ y + x **3 /3)

b = 1 + math.atan(z/2)**2

print(a)
print(b)
