direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def dfs(i, j, day):
    day += 1
    arr[i][j] = 2
    for dx, dy in direction:
        ni, nj = i + dx, j + dy
        if 0 <= ni < M and 0 <= nj < N:
            if arr[ni][nj] == 0 or arr[ni][nj] == 1:
                dfs()


M, N, H = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

d = 0

for i in range(M):
    for j in range(N):
        if arr[i][j] == 1:
            dfs(i, j, d)