from collections import deque
import sys
input = sys.stdin.readline

def dfs(start):
    visited_dfs[start] = 1
    result_dfs.append(start)
    
    for end in sorted(graph[start]):
        if not visited_dfs[end]:
            dfs(end)

def bfs(start):
    Q = deque([start])
    visited_bfs[start] = 1
    result_bfs.append(start)

    while Q:
        end = Q.popleft()
        for i in sorted(graph[end]):
            if not visited_bfs[i]:
                Q.append(i)
                result_bfs.append(i)
                visited_bfs[i] = 1

N, M, V = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited_dfs = [0] * (N + 1)
visited_bfs = [0] * (N + 1)

result_dfs = []
result_bfs = []

dfs(V)
bfs(V)

print(*result_dfs)
print(*result_bfs)