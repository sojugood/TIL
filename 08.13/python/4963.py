import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

direction = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

def dfs(i, j):
    arr[i][j] = 0
    for dx, dy in direction:
        ni, nj = i + dx, j + dy
        if 0 <= ni < h and 0 <= nj < w:
            if arr[ni][nj] == 1:
                dfs(ni, nj)

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    arr = [list(map(int, input().split())) for _ in range(h)]
    count = 0
    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1:
                count += 1
                dfs(i, j)
    print(count)