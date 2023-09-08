import sys
input = sys.stdin.readline
from collections import deque

direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def bfs():
    temp = 0
    tmpq = deque([])
    while q:
        x, y, cnt = q.popleft()
        if cnt > temp:
            for dx, dy in direction:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < M:
                    if arrs[nx][ny] > 0:

            arr = [row[:] for row in arrs]
            temp = cnt
        tmp = 0
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny] == 0:
                    tmp += 1
        arrs[x][y] -= tmp
        if arrs[x][y] > 0:
            q.append((x, y, cnt + 1))
        

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
arrs = [row[:] for row in arr]

q = deque([])

for i in range(N):
    for j in range(M):
        if arr[i][j] != 0:
            q.append((i, j, 0))

