import math
y = int(input("y: "))
x = int(input("x: "))
if x >= -9 and x < -6:
    y1 = math.sqrt(9-(x+6)**2)
    y2 = -3 + y1
    print(y2)
elif x>= -6 and x < -3:
    y3 = x + 3
    print(y3)
elif x>= -6 and x < 3:
    y4 = 3 + y1
    print(y4)
elif x >= 0 and x < 3:
    y6 = -x + 3
    print(y6)
elif x >= 3 and x < 9:
    y5 = x -6
    print(y5)
else:
    print("sorry")
