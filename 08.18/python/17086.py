from collections import deque
import sys
input = sys.stdin.readline

direction = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

def bfs(i, j):
    Q = deque([(i, j, 0)])
    visited = [[0] * M for _ in range(N)]
    visited[i][j] = 1
    while Q:
        x, y, depth = Q.popleft()
        for dx, dy in direction:
            ni, nj = x + dx, y + dy
            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
                if arr[ni][nj] == 0:
                    Q.append((ni, nj, depth + 1))
                    visited[ni][nj] = 1
                else:
                    return depth + 1


N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

max_depth = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            d = bfs(i, j)
            if d > max_depth:
                max_depth = d
print(max_depth)