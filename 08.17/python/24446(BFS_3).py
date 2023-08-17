from collections import deque
import sys
input = sys.stdin.readline

def bfs(start):
    Q = deque([(start, 0)])
    visited[start] = 0
    
    while Q:
        v, depth = Q.popleft()
        for i in graph[v]:
            if visited[i] == -1:
                Q.append((i, depth + 1))
                visited[i] = depth + 1

N, M, R = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [-1] * (N + 1)

bfs(R)

for i in visited[1:]:
    print(i)