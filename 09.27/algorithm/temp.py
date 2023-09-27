import sys
input = sys.stdin.readline

def getParent(parent, x):
    if parent[x] == x:
        return x
    parent[x] = getParent(parent, parent[x])
    return parent[x]


def unionParent(parent, a, b):
    a = getParent(parent, a)
    b = getParent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())

edges = []
for _ in range(m):
    x, y, c = map(int, input().split())
    edges.append((c, x, y))

edges.sort()

parent = [i for i in range(n + 1)]
total_distance = 0

for edge in edges:
    c, x, y = edge
    if getParent(parent, x) != getParent(parent, y):
        total_distance += c
        unionParent(parent, x, y)

print(total_distance)