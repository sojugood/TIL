import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(top):
    for bot in tree[top]:
        if not connect_lst[bot]:
            connect_lst[bot] = top
            dfs(bot)

N = int(input())

tree = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

connect_lst = [0] * (N + 1)

dfs(1)

for i in range(2, N + 1):
    print(connect_lst[i])