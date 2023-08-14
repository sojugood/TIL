import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def dfs(i, j, v):
    temp[i][j] = 0
    for dx, dy in direction:
        ni, nj = i + dx, j + dy
        if 0 <= ni < N and 0 <= nj < N:
            if temp[ni][nj] > v:
                dfs(ni, nj, v)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
temp = [row[:] for row in arr]
max_v = 0
for i in arr:
    t = max(i)
    if t > max_v:
        max_v = t
max_cnt = 0
for i in range(max_v):
    cnt = 0
    for j in range(N):
        for k in range(N):
            if temp[j][k] > i:
                cnt += 1
                dfs(j, k, i)
    if cnt > max_cnt:
        max_cnt = cnt
    temp = [row[:] for row in arr]
print(max_cnt)