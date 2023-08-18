from collections import deque

direction_1 = [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (-1, 1)]
direction_2 = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (1, 1)]

def bfs(i, j, arr):
    lst = []
    Q = deque([(i, j, 1, arr[i][j])])
    arr[i][j] = 0
    while Q:
        x, y, depth, v = Q.popleft()
        if depth == 4:
            lst.append(v)
            continue
        if y % 2 == 0:
            for dx, dy in direction_1:
                ni, nj = x + dx, y + dy
                if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] != 0:
                    v += arr[ni][nj]
                    Q.append((ni, nj, depth + 1, v))
                    arr[ni][nj] = 0
        elif y % 2 == 1:
            for dx, dy in direction_2:
                ni, nj = x + dx, y + dy
                if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] != 0:
                    v += arr[ni][nj]
                    Q.append((ni, nj, depth + 1, v))
                    arr[ni][nj] = 0
    return lst


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    Arr = [list(map(int, input().split())) for _ in range(N)]
    arr = [row[:] for row in Arr]
    result_lst = []
    for i in range(N):
        for j in range(M):
            result_lst.append((bfs(i, j, arr)))
    print(result_lst)
