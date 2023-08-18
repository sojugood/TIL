from collections import deque

def bfs(start):
    Q = deque([(start, 0)])
    visited[start] = 0

    while Q:
        start, depth = Q.popleft()
        for end in graph[start]:
            if visited[end] == -1:
                Q.append((end, depth + 1))
                visited[end] = depth + 1

T = int(input())

for tc in range(1, T + 1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    S, G = map(int, input().split())
    visited = [-1] * (V + 1)
    bfs(S)
    if visited[G] >= 0:
        result = visited[G]
    else:
        result = 0
    print(f"#{tc} {result}")