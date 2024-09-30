x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))
if (x > y and z > y ):
    if z > x:
        print(f"max: {x}")
    elif x > z:
        print(f"max: {z}")
elif (y > x and y > z):
    print(f"max: {y}")
elif (x < y and z > y):
    if y > z:
        print(f"max: {y}")
    elif z > y:
        print(f"max: {z}")
        












