import math 
x = int(input("Введите число: "))
y = int(input("Введите число: "))
z = int(input("Введите число: ")) 
if z >= y:
    
    
    if y >= x:
        print(x*2, y*2, z*2)
    else:
        print(abs(x))
        print(abs(y))
        print(abs(z))

else:
    print(abs(x))
    print(abs(y))
    print(abs(z))