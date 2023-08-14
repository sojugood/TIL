import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(start):
    global order
    visited[start] = order
    for next in sorted(graph[start]):
        if not visited[next]:
            order += 1
            dfs(next)

N, M, R = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
visited = [0] * (N + 1)
order = 1
dfs(R)
for i in range(1, N + 1):
    print(visited[i])