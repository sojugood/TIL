direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def dfs(i, j, cnt, move):
    if board[i][j] == 1:
        cnt += 1
    if move == 3:
        if cnt >= 2:
            return 1
        else:
            return 0
    for dx, dy in direction:
        ni, nj = i + dx, j + dy
        if 0 <= ni < 5 and 0 <= nj < 5 and board[ni][nj] != -1:
            temp = board[i][j]
            board[i][j] = -1
            if dfs(ni, nj, cnt, move + 1):
                return 1
            board[i][j] = temp
    return 0

board = [list(map(int, input().split())) for _ in range(5)]

r, c = map(int, input().split())

result = dfs(r, c, 0, 0)

print(result)