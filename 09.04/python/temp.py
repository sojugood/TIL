import sys
input = sys.stdin.readline
from collections import deque

direction = [1, -1]

def bfs(start, end):
    q = deque([(start, 0)])
    visited = [float("inf")] * (N + 1)
    visited[start] = 0

    while q:
        x, cnt = q.popleft()
        if x == end:
            return cnt
        if port[x]:
            for next in port[x]:
                if visited[next] > cnt + 1:
                    visited[next] = cnt + 1
                    q.append((next, cnt + 1))
        for dx in direction:
            nx = x + dx
            if 0 < nx <= N and cnt + 1 < visited[nx]:
                visited[nx] = cnt + 1
                q.append((nx, cnt + 1))


N, M = map(int, input().split())

S, E = map(int, input().split())

port = [[] for _ in range(N + 1)]

for _ in range(M):
    x, y = map(int, input().split())
    port[x].append(y)
    port[y].append(x)

print(bfs(S, E))