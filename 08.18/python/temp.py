from collections import deque
import sys
input = sys.stdin.readline

def dfs(start):
    dfs_visited[start] = 1
    dfs_lst.append(start)
    for end in sorted(graph[start]):
        if not dfs_visited[end]:
            dfs(end)

def bfs(start):
    Q = deque([start])
    bfs_visited[start] = 1
    bfs_lst.append(start)
    while Q:
        s = Q.popleft()
        for end in sorted(graph[s]):
            if not bfs_visited[end]:
                Q.append(end)
                bfs_visited[end] = 1
                bfs_lst.append(end)

N, M, V = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

dfs_visited = [0] * (N + 1)
bfs_visited = [0] * (N + 1)

dfs_lst = []
bfs_lst = []

dfs(V)
bfs(V)

print(*dfs_lst)
print(*bfs_lst)