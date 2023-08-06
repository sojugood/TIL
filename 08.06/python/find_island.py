directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# 깊이 우선 탐색(DFS)
def mark_island(i, j):
    arr[i][j] = 0
    for di, dj in directions:
        ni, nj = i + di, j + dj
        if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 1:
            mark_island(ni, nj)

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                count += 1
                mark_island(i, j)
    print(f"#{tc} {count}")