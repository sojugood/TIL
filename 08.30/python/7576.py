from collections import deque

direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def bfs():
    res = 0
    q = deque([])
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                q.append((i, j, 0))
    
    while q:
        x, y, day = q.popleft()

        for dx, dy in direction:
            ni, nj = x + dx, y + dy
            if 0 <= ni < N and 0 <= nj < M:
                if arr[ni][nj] == 0:
                    arr[ni][nj] = 1
                    q.append((ni, nj, day + 1))
        
        if not q:
            res = day
    return res


M, N = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

result = bfs()

for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            result = -1
            break

print(result)