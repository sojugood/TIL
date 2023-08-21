direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def dfs(i, j, fuel, visited):
    global result
    if fuel >= result:
        return
    if i == N - 1 and j == N - 1:
        result = min(result, fuel)
        return

    visited[i][j] = True
    h = arr[i][j]

    for dx, dy in direction:
        ni, nj = i + dx, j + dy
        if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
            diff = arr[ni][nj] - h
            if diff > 0:
                dfs(ni, nj, fuel + (diff * 2), visited)
            elif diff == 0:
                dfs(ni, nj, fuel + 1, visited)
            else:
                dfs(ni, nj, fuel, visited)

    if (i, j) in tunnel_map:
        ni, nj, C = tunnel_map[(i, j)]
        if not visited[ni][nj]:
            dfs(ni, nj, fuel + C, visited)

    visited[i][j] = False

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [[False] * N for _ in range(N)]
    tunnel_map = {}
    for _ in range(M):
        Ai, Aj, Bi, Bj, C = map(int, input().split())
        tunnel_map[(Ai-1, Aj-1)] = (Bi-1, Bj-1, C)
        tunnel_map[(Bi-1, Bj-1)] = (Ai-1, Aj-1, C)

    result = float("inf")
    dfs(0, 0, 0, visited)
    print(f"#{tc} {result}")
