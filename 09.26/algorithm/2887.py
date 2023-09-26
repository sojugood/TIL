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

N = int(input())

planets = []
for i in range(N):
    x, y, z = map(int, input().split())
    planets.append((x, y, z, i))

edges = []

# x, y, z 각각의 좌표로 정렬하면서 인접한 행성들만 고려
for i in range(3):
    planets.sort(key=lambda x: x[i])
    for j in range(1, N):
        edges.append((abs(planets[j-1][i] - planets[j][i]), planets[j-1][3], planets[j][3]))

edges.sort()

parent = [i for i in range(N)]
total_distance = 0

for edge in edges:
    cost, a, b = edge
    if getParent(parent, a) != getParent(parent, b):
        total_distance += cost
        unionParent(parent, a, b)

print(total_distance)
