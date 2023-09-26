from collections import deque

direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def bfs(i, j, island_num):
    q = deque([(i, j)])
    visited[i][j] = island_num
    boundary_points = []

    while q:
        x, y = q.popleft()

        is_boundary = False

        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if arr[nx][ny] == 0:
                    is_boundary = True
                elif arr[nx][ny] == 1:
                    visited[nx][ny] = island_num
                    q.append((nx, ny))
        if is_boundary:
            boundary_points.append((x, y))

    return boundary_points

def bfs2(num):
    q = deque([])
    check = [[0] * N for _ in range(N)]
    for x, y in boundary_lst[num - 1]:
        q.append((x, y, 0))
        check[x][y] = 1

    while q:
        x, y, cnt = q.popleft()
        if visited[x][y] != 0 and visited[x][y] != num:
            return cnt - 1
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and not check[nx][ny]:
                if visited[nx][ny] != num:
                    q.append((nx, ny, cnt + 1))
                    check[nx][ny] = 1



N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

visited = [[0] * N for _ in range(N)]

boundary_lst = []

island_num = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and not visited[i][j]:
            island_num += 1
            points = bfs(i, j, island_num)
            boundary_lst.append(points)

res = float('inf')

for i in range(island_num):
    res = min(res, bfs2(i + 1))

print(res)
