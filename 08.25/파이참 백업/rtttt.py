direction = {0: [(-1, 0, 1), (0, -1, 0), (1, 0, 3), (0, 1, 2)],
             1: [(0, 1, 2), (-1, 0, 1), (0, -1, 0), (1, 0, 3)],
             2: [(1, 0, 3), (0, 1, 2), (-1, 0, 1), (0, -1, 0)],
             3: [(0, -1, 0), (1, 0, 3), (0, 1, 2), (-1, 0, 1)]}


def dfs(arrs, i, j, rot, day, cnt, k, lst):

    if day == 0:
        return cnt

    for _ in range(len(lst)):
        x, y, w = lst.pop(0)
        w -= 1
        if w == 0:
            arrs[x][y] = 2
            continue
        elif w == 1:
            arrs[x][y] = 3
            lst.append((x, y, w))
        else:
            lst.append((x, y, w))

    if arrs[i][j] == 0:
        for dx, dy, r in direction[rot]:
            ni, nj = i + dx, j + dy
            if 0 <= ni < N and 0 <= nj < N:
                if arrs[ni][nj] != 1:
                    arrs[i][j] = 1
                    lst.append((i, j, 3))
                    return dfs(arrs, ni, nj, r, day - 1, cnt, k, lst)

        else:
            return dfs(arrs, i, j, rot, day - 1, cnt, k, lst)

    elif arrs[i][j] == 2:
        for dx, dy, r in direction[rot]:
            ni, nj = i + dx, j + dy
            if 0 <= ni < N and 0 <= nj < N:
                if arrs[ni][nj] != 1:
                    arrs[i][j] = 0
                    return dfs(arrs, ni, nj, r, day - 1, cnt + 1, k, lst)

        else:
            arrs[i][j] = 0
            return dfs(arrs, i, j, rot, day - 1, cnt + 1, k, lst)
    return dfs(arrs, i, j, rot, day - 1, cnt, k, lst)


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                for l in range(4):
                    arrs = [row[:] for row in arr]
                    lst = []
                    k = 1
                    result = max(result, dfs(arrs, i, j, l, M, 0, k, lst))
    print(f"#{tc} {result}")
