import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def dfs(node, order):
    global cnt
    visited[node] = True
    order[node] = cnt
    cnt += 1

    for next_node in adj[node]:
        if not visited[next_node]:
            dfs(next_node, order)

N, M, R = map(int, input().split())

adj = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

for i in range(1, N+1):
    adj[i].sort(reverse=True)

visited = [False] * (N+1)
order = [0] * (N+1)
cnt = 1

dfs(R, order)

for i in range(1, N+1):
    print(order[i])