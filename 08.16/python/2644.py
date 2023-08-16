import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(start, f):
    if visited[start]:
        return
    
    visited[start] = f
    for end in graph[start]:
        if not visited[end]:
            dfs(end, f + 1)

N = int(input())

s, e = map(int, input().split())

M = int(input())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [0] * (N + 1)

dfs(s, 0)

if visited[e]:
    print(visited[e])
else:
    print(-1)