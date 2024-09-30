import math
a = float(input("введите первую координату: "))
b = float(input("введите вторую координату: "))
c = float(input("введите третью координату: "))
d = float(input("введите четвертую координату: "))

"""def r(a,b,c,d):
    return (a + b) - (c + d)
print(r(a,b,c,d))"""

n = ((b+a) ** 2) + ((d + c) ** 2)
m = math.sqrt(n)
print(m)
