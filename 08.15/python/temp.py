def dfs(start, num):
    visited[start] = num
    for end in arr[start]:
        if visited[end] == -1:
            dfs(end, num + 1)

N, K = map(int, input().split())

arr = [[] for _ in range(N)]

for i in range(N):
    arr[i].append(int(input()))

visited = [-1] * N

dfs(0, 0)

print(visited[K])