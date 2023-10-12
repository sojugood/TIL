from collections import deque

direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def bfs(i, j):
    q = deque([(i, j, 0, None, set())])
    while q:
        x, y, cnt, cannot, tmp = q.popleft()
        if len(tmp) == 2:
            return cnt

        for dx, dy in direction:
            if (dx, dy) == cannot:
                continue
            else:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] != '#':
                    if arr[nx][ny] == 'C':
                        ttmp = {(nx, ny)}
                        q.append((nx, ny, cnt + 1, (dx, dy) ,tmp | ttmp))
                    else:
                        q.append((nx, ny, cnt + 1, (dx, dy) ,tmp))
    return -1

N, M = map(int, input().split())

arr = [list(map(str, input().strip())) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if arr[i][j] == 'S':
            arr[i][j] = '.'
            res = bfs(i, j)
            break

print(res)