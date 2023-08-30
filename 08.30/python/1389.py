from collections import deque

def bfs(start, end):
    visited = [0] * (N + 1)
    q = deque([(start, 0)])
    while q:
        next, depth = q.popleft()
        if next == end:
            return depth
        for nnext in lst[next]:
            if not visited[nnext]:
                visited[nnext] = 1
                q.append((nnext, depth + 1))

N, M = map(int, input().split())

lst = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    lst[u].append(v)
    lst[v].append(u)

res = float("inf")
result = None

for i in range(1, N + 1):
    tmp = 0
    for j in range(1, N + 1):
        if j == i:
            continue
        else:
            tmp += bfs(i, j)
    if tmp < res:
        res = tmp
        result = i

print(result)