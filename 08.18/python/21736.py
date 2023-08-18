from collections import deque
import sys
input = sys.stdin.readline

direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def bfs(i, j):
    cnt = 0
    Q = deque([(i, j)])
    while Q:
        x, y = Q.popleft()
        for dx, dy in direction:
            ni, nj = x + dx, y + dy
            if 0 <= ni < N and 0 <= nj < M:
                if arr[ni][nj] == 'O':
                    Q.append((ni, nj))
                    arr[ni][nj] = 'X'
                elif arr[ni][nj] == 'P':
                    Q.append((ni, nj))
                    arr[ni][nj] = 'X'
                    cnt += 1
    return cnt

N, M = map(int, input().split())

arr = [list(map(str, input().strip())) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if arr[i][j] == 'I':
            result = bfs(i, j)
            break
    else:
        continue
    break

if result > 0:
    print(result)
else:
    print('TT')