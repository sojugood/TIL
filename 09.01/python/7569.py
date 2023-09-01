import sys
input = sys.stdin.readline
from collections import deque

direction = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]


def bfs(q):

    while q:
        x, y, z, day = q.popleft()

        for dx, dy, dz in direction:
            ni, nj, nz = x + dx, y + dy, z + dz
            if 0 <= ni < N and 0 <= nj < M and 0 <= nz < H:
                if arr[nz][ni][nj] == 0:
                    arr[nz][ni][nj] = 1
                    q.append((ni, nj, nz, day + 1))

    for k in range(H):
        for i in range(N):
            for j in range(M):
                if arr[k][i][j] == 0:
                    return -1

    return day


M, N, H = map(int, input().split())

arr = [[[0] * M for _ in range(N)] for _ in range(H)]

q = deque()

for h in range(H):
    for i in range(N):
        temp = list(map(int, input().split()))
        for j in range(M):
            arr[h][i][j] = temp[j]
            if temp[j] == 1:
                q.append((i, j, h, 0))

print(bfs(q))