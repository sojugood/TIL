from collections import deque
import sys
input = sys.stdin.readline

direction = [(-1, 0), (0, -1), (1, 0), (0, 1)]

def bfs(i, j):
    q = deque([])
    visited = [[-1] * M for _ in range(N)]
    for k in range(N):
        for l in range(M):
            if arr[k][l] == 0:
                visited[k][l] = 0
    q.append((i, j, 0))
    visited[i][j] = 0
    while q:
        x, y, cnt = q.popleft()
        for dx, dy in direction:
            ni, nj = x + dx, y + dy
            if 0 <= ni < N and 0 <= nj < M:
                if arr[ni][nj] == 1 and visited[ni][nj] == -1:
                    visited[ni][nj] = cnt + 1
                    q.append((ni, nj, cnt + 1))

    return visited

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            res = bfs(i, j)
            break

for i in res:
    print(*i)