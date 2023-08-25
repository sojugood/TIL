import sys
sys.setrecursionlimit(10**6)

di = [1, -1]

def dfs(start):
    visited[start] = 1
    k = Ai[start]
    for d in di:
        next = start + d * k
        if 1 <= next <= n and not visited[next]:
            dfs(next)


n = int(input())

Ai = [0] + list(map(int, input().split()))

s = int(input())

visited = [0] * (n + 1)

dfs(s)

print(sum(visited))