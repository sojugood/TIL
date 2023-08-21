direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def dfs(i, j):
    total = arr[i][j]
    for dx, dy in direction:
        for k in range(1, arr[i][j] + 1):
            ni, nj = i + dx*k, j + dy*k
            if 0 <= ni < N and 0 <= nj < M:
                total += arr[ni][nj]
    return total

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_v = 0
    for i in range(N):
        for j in range(M):
            temp = dfs(i, j)
            if temp > max_v:
                max_v = temp
    print(f"#{tc} {max_v}")
