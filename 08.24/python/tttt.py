direction = {0: [(-1, 0, 1), (0, -1, 0), (1, 0, 3), (0, 1, 2)],
             1: [(0, 1, 2), (-1, 0, 1), (0, -1, 0), (1, 0, 3)],
             2: [(1, 0, 3), (0, 1, 2), (-1, 0, 1), (0, -1, 0)],
             3: [(0, -1, 0), (1, 0, 3), (0, 1, 2), (-1, 0, 1)]}


def dfs(arrs, i, j, rot, day, cnt):
    global k

    if day == 0:
        return cnt

    for _ in range(len(lst)):
        x, y, w = lst.pop(0)
        w -= 1
        if w == 0:
            arrs[x][y] = 2
            continue
        else:
            lst.append((x, y, w))

    if arrs[i][j] == 0:
        for dx, dy, r in direction[rot]:
            ni, nj = i + dx, j + dy
            if 0 <= ni < N and 0 <= nj < N:
                if arrs[ni][nj] != 1:
                    arrs[i][j] = 1
                    lst.append((i, j, k + 3))
                    k += 1
                    dfs(arrs, ni, nj, r, day - 1, cnt)
                    break
                else:
                    continue
        else:
            dfs(arrs, i, j, rot, day - 1, cnt)

    elif arrs[i][j] == 2:
        for dx, dy, r in direction[rot]:
            ni, nj = i + dx, j + dy
            if 0 <= ni < N and 0 <= nj < N:
                if arrs[ni][nj] != 1:
                    arrs[i][j] = 0
                    dfs(arrs, ni, nj, r, day - 1, cnt + 1)
                    break
                else:
                    break
        else:
            arrs[i][j] = 0
            dfs(arrs, i, j, rot, day - 1, cnt + 1)
    dfs(arrs, i, j, rot, day - 1, cnt)


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    test = set()
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                for l in range(4):
                    arrs = [row[:] for row in arr]
                    lst = []
                    k = 1
                    result = max(result, dfs(arrs, i, j, l, M, 0))
    print(f"#{tc} {result}")
    print(test)