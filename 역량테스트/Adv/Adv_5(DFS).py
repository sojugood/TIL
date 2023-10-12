direction1 = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (1, 1)]
direction2 = [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (-1, 1)]
direction3 = [[(0, -1), (1, 0), (0, 1)], [(-1, 0), (1, -1), (1, 1)]]
direction4 = [[(0, -1), (-1, 0), (0, 1)], [(-1, -1), (1, 0), (-1, 1)]]

def dfs(arr, i, j, total, visited, depth):
    global result
    if depth == 4 or total + ((4 - depth) * max_v) < result:
        result = max(result, total)
        return
    visited[i][j] = 1
    for dx, dy in direction1 if j % 2 == 1 else direction2:
        ni, nj = i + dx, j + dy
        if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
            dfs(arr, ni, nj, total + arr[ni][nj], visited, depth + 1)
    visited[i][j] = 0

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    max_v = max(max(row) for row in arr)
    result = 0
    for i in range(N):
        for j in range(M):
            dfs(arr, i, j, arr[i][j], visited, 1)

            for dir in direction3 if j % 2 == 1 else direction4:
                temp = arr[i][j]
                for dx, dy in dir:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < N and 0 <= nj < M:
                        temp += arr[ni][nj]
                    else:
                        break
                result = max(result, temp)

    answer = result
    print(f"#{tc} {answer}")