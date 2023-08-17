import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def dfs(i, j):
    arr[i][j] = 2
    for dx, dy in direction:
        ni, nj = i + dx, j + dy
        if 0 <= ni < M and 0 <= nj < N:
            if arr[ni][nj] == 0:
                dfs(ni, nj)

M, N = map(int, input().split())

arr = [list(map(int, input().strip())) for _ in range(M)]

result = 'NO'

for j in range(N):
    if arr[0][j] == 0:
        dfs(0, j)
for i in range(N):
    if arr[M - 1][i] == 2:
        result = 'YES'

print(result)