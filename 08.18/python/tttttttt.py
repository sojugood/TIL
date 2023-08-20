from collections import deque

direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def bfs(i, j):
    Q = deque([(i, j)])
    arr[i][j] = '.'

    while Q:
        x, y = Q.popleft()
        for dx, dy in direction:
            ni, nj = x + dx, y + dy
            if 0 <= ni < H and 0 <= nj < W and arr[ni][nj] == '#':
                arr[ni][nj] = '.'
                Q.append((ni, nj))


T = int(input())

for _ in range(T):
    H, W = map(int, input().split())
    arr = [list(map(str, input().strip())) for _ in range(H)]
    cnt = 0
    for i in range(H):
        for j in range(W):
            if arr[i][j] == '#':
                cnt += 1
                bfs(i, j)
    print(cnt)