while True:
    a, b, c = map(int, input().split())
    if c == 0 and b == 0 and a == 0:
        break
    elif (c ** 2) == (b ** 2) + (a ** 2) or (b ** 2) == (c ** 2) + (a ** 2) or (a ** 2) == (b ** 2) + (c ** 2):
        print('right')
    else:
        print('wrong')