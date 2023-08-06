import math
sqrt = math.sqrt
T = int(input())

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    r = sqrt((y1 - y2) ** 2 + (x1 -x2) ** 2)
    if x1 == x2 and y1 == y2:
        if r1 == 0 and r2 == 0:
            print(1)
        elif r1 == r2:
            print(-1)
        else:
            print(0)
    elif abs(r1 - r2) < r < r1 + r2:
        print(2)
    elif r == r1 + r2 or r == abs(r1 - r2):
        print(1)
    else:
        print(0)