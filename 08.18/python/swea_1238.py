from collections import deque

def bfs(start):
    Q = deque([(start, 0)])
    visited[start] = 0

    while Q:
        start, depth = Q.popleft()
        for end in set(graph[start]):
            if visited[end] == -1:
                Q.append((end, depth + 1))
                visited[end] = depth + 1


for tc in range(1, 11):
    E, S = map(int, input().split())
    graph = [[] for _ in range(101)]
    edge = list(map(int, input().split()))
    for i in range(0, E, 2):
        u, v = edge[i], edge[i + 1]
        graph[u].append(v)

    visited = [-1] * (101)
    bfs(S)
    max_depth = [0, None]
    for j in range(101):
        if visited[j] >= max_depth[0]:
            max_depth = [visited[j], j]

    print(f"#{tc} {max_depth[-1]}")