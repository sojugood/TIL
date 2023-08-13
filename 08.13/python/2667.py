import sys
sys.setrecursionlimit(10**6)

direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def dfs(i, j):
    global cnt
    cnt += 1
    arr[i][j] = 0
    for dx, dy in direction:
        ni, nj = i + dx, j + dy
        if 0 <= ni < N and 0 <= nj < N:
            if arr[ni][nj] == 1:
                dfs(ni, nj)

N = int(input())
arr = [[] for _ in range(N)]
for k in range(N):
    n = input()
    for i in n:
        arr[k].append(int(i))
house = 0
cnt = 0
lst = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            house += 1
            dfs(i, j)
            lst.append(cnt)
            cnt = 0
lst.sort()
print(house)
for k in lst:
    print(k)