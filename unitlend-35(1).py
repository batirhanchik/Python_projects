x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))

if (x > y and x > z):
    print(x + y + z, "max x: ", x)
elif (y > x and y > z):
    print(x + y + z, "max y: ", y)
elif (z > x and z > y):
    print(x + y + z, "max z: ", z)

