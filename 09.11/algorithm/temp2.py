from collections import deque
import sys
input = sys.stdin.readline

direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def bfs(i, j):
    visited = [[0] * M for _ in range(N)]
    visited[i][j] = 1
    q = deque([])
    q.append((i, j, 0))

    while q:
        x, y, cnt = q.popleft()

        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if arr[nx][ny] == 'L':
                    visited[nx][ny] = 1
                    q.append((nx, ny, cnt + 1))
    
    return cnt

N, M = map(int, input().split())

arr = [list(map(str, input().strip())) for _ in range(N)]

result = 0

for i in range(N):
    for j in range(M):
        if arr[i][j] == 'L':
            result = max(result, bfs(i, j))

print(result)