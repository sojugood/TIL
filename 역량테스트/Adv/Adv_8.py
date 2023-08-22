from collections import deque

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def find(limit_jump):
    visited = [[False] * M for _ in range(N)]
    queue = deque([(start_i, start_j)])
    visited[start_i][start_j] = True

    while queue:
        i, j = queue.popleft()

        for dx, dy in directions:
            if dx:  # 상하(행) 이동인 경우
                for k in range(1, limit_jump + 1):
                    ni, nj = i + dx * k, j
                    if 0 <= ni < N and not visited[ni][j]:
                        if arr[ni][j] == 1:
                            visited[ni][j] = True
                            queue.append((ni, nj))
                        elif arr[ni][j] == 3:
                            return True
            else:  # 좌우(열) 이동인 경우
                ni, nj = i, j + dy
                if 0 <= nj < M and not visited[i][nj]:
                    if arr[i][nj] == 1:
                        visited[i][nj] = True
                        queue.append((ni, nj))
                    elif arr[i][nj] == 3:
                        return True

    return False

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            start_i, start_j = i, j

low, high, ans = 1, N, N

while low <= high:
    mid = (low + high) // 2
    if find(mid):
        ans = mid
        high = mid - 1
    else:
        low = mid + 1

print(ans)
