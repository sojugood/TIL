from collections import deque
import sys
input = sys.stdin.readline

def bfs(start):
    num = 1
    Q = deque([(start, 0)])
    lst[start] = num
    visited[start] = 0
    
    while Q:
        v, depth = Q.popleft()
        for i in sorted(graph[v]):
            if visited[i] == -1:
                Q.append((i, depth + 1))
                num += 1
                lst[i] = num
                visited[i] = depth + 1

N, M, R = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

lst = [0] * (N + 1)
visited = [-1] * (N + 1)

bfs(R)

result = 0
for i in range(1, N + 1):
    result += (lst[i] * visited[i])

print(result)