def dfs(start):
    visited[start] = 1
    for end in arr[start]:
        if not visited[end]:
            dfs(end)

N = int(input())

E = int(input())

arr = [[] for _ in range(N + 1)]

for _ in range(E):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)

visited = [0] * (N + 1)

dfs(1)

print(sum(visited) - 1)