from collections import deque
import sys
input = sys.stdin.readline

direction = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

def bfs(lst):
    Q = deque(lst)
    while Q:
        x, y = Q.popleft()
        for dx, dy in direction:
            ni, nj = x + dx, y + dy
            if 0 <= ni < N and 0 <= nj < M and not arr[ni][nj]:
                Q.append((ni, nj))
                arr[ni][nj] = arr[x][y] + 1


N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

shark_lst = []

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            shark_lst.append((i, j))
bfs(shark_lst)

result = max(map(max, arr))

print(result - 1)