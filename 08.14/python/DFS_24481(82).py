import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(start, depth):
    depth += 1
    visited[start] = depth
    for next in sorted(graph[start]):
        if visited[next] == -1:
            dfs(next, depth)

N, M, R = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
visited = [-1] * (N + 1)
dfs(R, -1)
for i in range(1, N + 1):
    print(visited[i])