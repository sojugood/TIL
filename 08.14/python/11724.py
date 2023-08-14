import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(start):
    global cnt
    for end in arr[start]:
        if not visited[end]:
            cnt += 1
            visited[end] = 1
            dfs(end)

N, M = map(int, input().split())
arr = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)
visited = [0] * (N + 1)
count = 0
for i in range(1, N + 1):
    cnt = 0
    dfs(i)
    if cnt > 0:
        count += 1
for j in range(1, N + 1):
    if visited[j] == 0:
        count += 1
print(count)