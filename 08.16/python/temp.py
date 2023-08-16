import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(o, t, cnt):

N = int(input())

a, b = map(int, input().split())

M = int(input())

tree = [[] for _ in range(N + 1)]

for _ in range(M):
    x, y = map(int, input().split())
    tree[x].append(y)
    tree[y].append(x)

print(dfs(a, b, 0))