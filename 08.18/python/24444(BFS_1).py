from collections import deque
import sys
input = sys.stdin.readline

def bfs(start):
    num = 1
    Q = deque([start])
    visited[start] = num
    
    while Q:
        v = Q.popleft()
        # print(v)

        for i in sorted(graph[v]):
            if not visited[i]:
                num += 1
                Q.append(i)
                visited[i] = num

N, M, R = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [0] * (N + 1)

bfs(R)

for i in visited[1:]:
    print(i)