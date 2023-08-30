import sys
sys.setrecursionlimit(10**6)

direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def dfs(i, j):
    temp = arr[i][j]
    arr[i][j] = 'C'
    
    for dx, dy in direction:
        ni, nj = i + dx, j + dy
        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == temp:
            dfs(ni, nj)

def dfs2(i, j):
    if arr2[i][j] == 'R' or arr2[i][j] == 'G':
        temp = ['R', 'G']
    else:
        temp = ['B']
    
    arr2[i][j] = 'C'
    
    for dx, dy in direction:
        ni, nj = i + dx, j + dy
        if 0 <= ni < N and 0 <= nj < N and arr2[ni][nj] in temp:
            dfs2(ni, nj)

N = int(input())

arr = [list(input()) for _ in range(N)]
arr2 = [row[:] for row in arr]

cnt = 0
cnt2 = 0

for i in range(N):
    for j in range(N):
        if arr[i][j] != 'C':
            cnt += 1
            dfs(i, j)

for i in range(N):
    for j in range(N):
        if arr2[i][j] != 'C':
            cnt2 += 1
            dfs2(i, j)

print(cnt, cnt2)
