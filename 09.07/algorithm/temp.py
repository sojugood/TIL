import sys
input = sys.stdin.readline
from collections import deque

direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def bfs():

    while q:
        x, y, cnt = q.popleft()
        
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

q = deque([])

for i in range(N):
    for j in range(M):
        if arr[i][j] != 0:
            q.append((i, j, 0))

