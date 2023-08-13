import sys
sys.setrecursionlimit(10**6)
def dfs(start, chk, order):
    if start == N + 1:
        return
    for end in arr[start]:
        if end == order + 1:
            chk[end] = end
    dfs(start + 1, chk, order + 1)

N, M, R = map(int, input().split())
arr = [[] for _ in range(N + 1)]
lst = [0] * (N + 1)
for _ in range(M):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)
lst[R] = 1
dfs(R, lst, 1)
for j in range(1, N + 1):
    print(lst[j])