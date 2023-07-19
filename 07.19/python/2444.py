n = int(input())

for i in range(1, (2 * n)):
    star = '*' * ((2 * i) - 1)
    if len(star) > 2 * n:
        for j in range(2, n + 1):
            star = '*' * (((2 * i) - 1) - (2 * j))
            space = ' ' * (j - 1)
            print(space + star)
        break
    else:
        space = ' ' * (n - i)
        print(space + star)
