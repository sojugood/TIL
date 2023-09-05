from collections import deque

direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def bfs(i, j):
    q = deque([])
    arr[i][j] = 0
    q.append((i, j))
    cnt = 1
    while q:
        x, y= q.popleft()
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 1:
                arr[nx][ny] = 0
                cnt += 1
                q.append((nx, ny))
    return cnt

n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

res = 0
result = 0

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            res += 1
            result = max(result ,bfs(i, j))

print(res)
print(result)