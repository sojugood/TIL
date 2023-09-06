import sys
input = sys.stdin.readline
from collections import deque

direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def bfs(i, j):
    arr[i][j] = 1
    q = deque([])
    q.append((i, j))
    cnt = 1
    while q:
        x, y = q.popleft()
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 0:
                arr[nx][ny] = 1
                cnt += 1
                q.append((nx, ny))
    return cnt

N, M, K = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

result = M

for i in range(N):
    for j in range(N):
        if arr[i][j] == 0:
            tmp = bfs(i, j)
            if tmp % K == 0:
                res = tmp // K
            else:
                res = tmp // K + 1
            result -= res


if result == M:
    print("IMPOSSIBLE")
elif result >= 0:
    print("POSSIBLE")
    print(result)
else:
    print("IMPOSSIBLE")