import sys
input = sys.stdin.readline

direction = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

def dfs(x, y):
    for dx, dy in direction:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            if arr[nx][ny] > arr[x][y]:
                return 0
            elif arr[nx][ny] == arr[x][y]:
                visited[x][y] = 1
                visited2[nx][ny] = 1
                tmp = dfs(nx, ny)
                visited[x][y] = 0
                if tmp == 0:
                    return 0
    return 1


N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

visited = [[0] * M for _ in range(N)]

visited2 = [[0] * M for _ in range(N)]

res = 0

for i in range(N):
    for j in range(M):
        if not visited2[i][j]:
            res += dfs(i, j)

print(res)