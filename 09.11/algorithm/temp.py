import sys
from collections import deque

input = sys.stdin.readline

direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def bfs():
    q = deque([(0, 0, 0, 0)])  # x, y, time, sword
    visited = [[[False] * 2 for _ in range(M)] for _ in range(N)]  # sword가 2개로 존재함
    visited[0][0][0] = True

    while q:
        x, y, t, sword = q.popleft()

        if x == N-1 and y == M-1:
            return t

        if t > T:
            continue

        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny] != 1 or (sword == 1 and not visited[nx][ny][sword]):
                    if arr[nx][ny] == 2 and not sword:
                        if not visited[nx][ny][1]:
                            visited[nx][ny][1] = True
                            q.append((nx, ny, t + 1, 1))
                    elif not visited[nx][ny][sword]:
                        visited[nx][ny][sword] = True
                        q.append((nx, ny, t + 1, sword))

    return -1

N, M, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
res = bfs()

if 0 <= res <= T:
    print(res)
else:
    print("Fail")
