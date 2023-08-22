direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
directions = [(1, 0), (-1, 0), (0, 1)], [(1, 0), (-1, 0), (0, -1)], [(1, 0), (0, -1), (0, 1)], [(-1, 0), (0, -1), (0, 1)]

def dfs(i, j, depth, total):
    global result
    if depth == 4 or total + (4 - depth) * max_v <= result:
        result = max(result, total)
        return
    visited[i][j] = 1
    for dx, dy in direction:
        ni, nj = i + dx, j + dy
        if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
            dfs(ni, nj, depth + 1, total + arr[ni][nj])
    visited[i][j] = 0

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

visited = [[0] * M for _ in range(N)]

max_v = max(max(row) for row in arr)

result = 0

for i in range(N):
    for j in range(M):
        dfs(i, j, 1, arr[i][j])
        for dir in directions:
            temp = arr[i][j]
            for dx, dy in dir:
                ni, nj = i + dx, j + dy
                if 0 <= ni < N and 0 <= nj < M:
                    temp += arr[ni][nj]
                else:
                    break
            result = max(result, temp)

print(result)