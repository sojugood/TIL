from collections import deque
import sys
input = sys.stdin.readline

def bfs(start):
    Q = deque([(start, 0)])
    visited[start] = 0

    while Q:
        n, depth = Q.popleft()
        if depth == K:
            break
        for end in graph[n]:
            if visited[end] == -1:
                Q.append((end, depth + 1))
                visited[end] = depth + 1


N, M, K, X = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)

visited = [-1] * (N + 1)

bfs(X)

result = []

for i in range(1, N + 1):
    if visited[i] == K:
        result.append(i)

if result:
    for j in result:
        print(j)
else:
    print(-1)