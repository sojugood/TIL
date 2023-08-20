direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
rotation = {0:[3, 2, 1, 0], 1:[0, 3, 2, 1], 2:[1, 0, 3, 2], 3:[2, 1, 0, 3]}

N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
cnt = 0

while True:
    if arr[r][c] == 0:
        arr[r][c] = 2
        cnt += 1
    for i in rotation[d]:
        ni, nj = r + direction[i][0], c + direction[i][-1]
        if arr[ni][nj] == 0:
            d = i
            r, c = ni, nj
            break
    else:
        if arr[r - direction[d][0]][c - direction[d][-1]] == 2:
            r, c = r - direction[d][0], c - direction[d][-1]
        else:
            break

print(cnt)