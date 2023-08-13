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

def dfs2(start, depth):
    depth += 1
    depth_lst[start] = depth
    for next in sorted(graph[start]):
        if depth_lst[next] == -1:
            dfs2(next, depth)

N, M, R = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
visited = [0] * (N + 1)
depth_lst = [-1] * (N + 1)
order = 1
dfs(R)
dfs2(R, -1)
result = 0
for i in range(1, N + 1):
    result += visited[i] * depth_lst[i]
print(result)