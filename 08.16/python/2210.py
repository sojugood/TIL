import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def dfs(i, j, depth, temp):
    temp += arr[i][j]
    depth += 1
    if depth == 6:
        result.add(temp)
        temp = ''
        return
    for dx, dy in direction:
        ni, nj = i + dx, j + dy
        if 0 <= ni < 5 and 0 <= nj < 5:
            dfs(ni, nj, depth, temp)

arr = [(input().split()) for _ in range(5)]

result = set()

temp = ''

for i in range(5):
    for j in range(5):
        dfs(i, j, 0, temp)

print(len(result))