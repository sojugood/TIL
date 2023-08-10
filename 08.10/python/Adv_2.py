dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(board, x, y, depth):
    if depth == 3:
        return
    global catch
    N = len(board)
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        jumped = False
        while 0 <= nx < N and 0 <= ny < N:
            # 쫄을 만날 경우
            if board[nx][ny] == 1:
                if jumped:
                    catch.add((nx, ny))
                    board[nx][ny] = 0
                    dfs(board, nx, ny, depth + 1)
                    board[nx][ny] = 1
                    break
                else:
                    jumped = True
                    nx += dx[i]
                    ny += dy[i]
            # 빈 칸일 경우
            else:
                if jumped:
                    dfs(board, nx, ny, depth + 1)
                    nx += dx[i]
                    ny += dy[i]
                else:
                    nx += dx[i]
                    ny += dy[i]
    return

T = int(input())
for t in range(T):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    catch = set()
    for i in range(N):
        for j in range(N):
            if board[i][j] == 2:
                board[i][j] = 0
                dfs(board, i, j, 0)
                break
    print(f"#{t + 1} {len(catch)}")
