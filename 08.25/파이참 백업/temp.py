direction = [(0, -1), (-1, 0)]

def dfs(i, j, depth, rr):
    if rr > depth:
        return
    if arr[i][j] == 1:
        visited[i][j] = 1

    for dx, dy in direction:
        for k in range(1, rr + 1):
            ni, nj = i + dx * k, j + dy * k
            if 0 <= ni < N + 1 and 0 <= nj < M and not visited[ni][nj]:
                if arr[ni][nj] == 1:
                    cnt += 1
                    visited[ni][nj] = 1



N, M, D = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
castle = [0] * M
arr.append(castle)

for j in range(M):
    visited = [[0] * M for _ in range(N)]
    bfs(N + 1, j, D, 1)

