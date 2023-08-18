from collections import deque
direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def bfs(i, j):
    Q = deque([(i, j, 0)])
    arr[i][j] = 1

    while Q:
        x, y, cnt = Q.popleft()
        for dx, dy in direction:
            ni, nj = x + dx, y + dy
            if 0 <= ni < N and 0 <= nj < N:
                if arr[ni][nj] == 0:
                    arr[ni][nj] = 1
                    Q.append((ni, nj, cnt + 1))
                elif arr[ni][nj] == 3:
                    return cnt
    return 0

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().strip())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                result = bfs(i, j)
    print(f"#{tc} {result}")