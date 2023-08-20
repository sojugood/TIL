import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def dfs(i, j):
    visited[i][j] = 1
    for dx, dy in direction:
        ni, nj = i + dx, j + dy
        if 0 <= ni < H and 0 <= nj < W and arr[ni][nj] == '#' and not visited[ni][nj]:
            dfs(ni, nj)

T = int(input())

for _ in range(T):
    H, W = map(int, input().split())
    arr = [list(input()) for _ in range(H)]
    visited = [[0] * W for _ in range(H)]
    cnt = 0
    for i in range(H):
        for j in range(W):
            if arr[i][j] == '#' and not visited[i][j]:
                cnt += 1
                dfs(i, j)
    print(cnt)