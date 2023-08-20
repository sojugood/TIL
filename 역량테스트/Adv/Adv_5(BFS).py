from collections import deque

direction_1 = [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (-1, 1)]
direction_2 = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (1, 1)]
direction_3 = [[(1, 0), (0, 1), (0, -1)], [(-1, 0), (0, 1), (0, -1)], [(1, 0), (-1, -1), (-1, 1)]]
direction_4 = [[(1, 0), (0, 1), (0, -1)], [(-1, 0), (0, 1), (0, -1)], [(-1, 0), (1, -1), (1, 1)]]


def bfs(arr, i, j, max_val):
    global total
    visited = [[False] * M for _ in range(N)]
    visited[i][j] = True
    queue = deque([(i, j, 1, arr[i][j], visited)])
    while queue:
        i, j, depth, v, visited = queue.popleft()

        if depth == 4 or v + (4 - depth) * max_val <= total:
            total = max(total, v)
            continue

        directions = direction_1 if j % 2 == 0 else direction_2
        for dx, dy in directions:
            ni, nj = i + dx, j + dy
            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
                new_visited = [row[:] for row in visited]
                new_visited[ni][nj] = True
                queue.append((ni, nj, depth + 1, v + arr[ni][nj], new_visited))


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_val = max(max(row) for row in arr)
    total = 0

    for i in range(N):
        for j in range(M):
            bfs(arr, i, j, max_val)
            dirs = direction_3 if j % 2 == 0 else direction_4
            for dir in dirs:
                temp = arr[i][j]
                for dx, dy in dir:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < N and 0 <= nj < M:
                        temp += arr[ni][nj]
                    else:
                        break
                total = max(total, temp)

    print(f"#{tc} {total}")
