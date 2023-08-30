from collections import deque
direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def bfs(i, j, cnt):
    q = deque([])
    visited = [[float("inf")] * M for _ in range(N)]
    visited[i][j] = 1
    q.append((i, j, cnt))

    while q:
        x, y, res = q.popleft()
        if x == N - 1 and y == M - 1:
            continue
        for dx, dy in direction:
            ni, nj = x + dx, y + dy
            if 0 <= ni < N and 0 <= nj < M and (res + 1) < visited[ni][nj] and arr[ni][nj] == 1:
                visited[ni][nj] = res + 1
                q.append((ni, nj, res + 1))
    return visited[N - 1][M - 1]

N, M = map(int, input().split())

arr = [list(map(int, input().strip())) for _ in range(N)]

visited = [[float("inf")] * M for _ in range(N)]

print(bfs(0, 0, 1))