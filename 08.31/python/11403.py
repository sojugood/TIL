from collections import deque
import sys
input = sys.stdin.readline

def bfs(start, end):
    q = deque([(start, 0)])
    visited = [0] * N
    visited[start] = 1

    while q:
        next, depth = q.popleft()
        for nnext in connect[next]:
            if nnext == end:
                return depth + 1
            if not visited[nnext]:
                visited[nnext] = 1
                q.append((nnext, depth + 1))
    return 0
N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

connect = [[] for _ in range(N)]

res_arr = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            connect[i].append(j)

for i in range(N):
    for j in range(N):
        if bfs(i, j) > 0:
            res_arr[i][j] = 1

for i in res_arr:
    print(*i)