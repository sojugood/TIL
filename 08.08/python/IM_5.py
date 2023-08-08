T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    map_list = [list(map(int, input().split())) for _ in range(N + 1)]
    house_list = []
    R = 0
    X = None
    Y = None
    for i in range(N + 1):
        for j in range(N + 1):
            if map_list[i][j] == 1:
                house_list.append((i, j))
            elif map_list[i][j] == 2:
                X, Y = i, j
    for x, y in house_list:
        D = ((X - x)**2 + (Y - y)**2)**0.5
        if D > R:
            R = D
    if int(R) == R:
        result = int(R)
    else:
        result = int(R) + 1
    print(f"#{tc} {result}")