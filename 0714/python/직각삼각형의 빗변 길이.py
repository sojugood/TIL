import math

a, b = map(int, input().split())

def hypotenuse(a, b):
    c = math.sqrt(a**2 + b**2)
    return round(c, 2)

print(hypotenuse(a, b))