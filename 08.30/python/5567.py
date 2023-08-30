n = int(input())

m = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (n + 1)

for i in graph[1]:
    if not visited[i]:
        visited[i] = 1
    for j in graph[i]:
        if not visited[j]:
            visited[j] = 1

visited[1] = 0
print(sum(visited))