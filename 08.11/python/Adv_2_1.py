direction = [(0, 1), (0, -1), (1, 0), (-1, 0)] # 포의 이동 방향

def dfs(board, x, y, depth): # DFS
    if depth > 3: # 이동 가능 횟수 도달 시 종료
        return
    global catch # 잡은 쫄의 좌표 저장하기 위한 set
    N = len(board)
    for dx, dy in direction:
        nx, ny = x + dx, y + dy
        jumped = False # 포가 처음 마주하는 쫄을 뛰어 넘었는지 확인
        while 0 <= nx < N and 0 <= ny < N:
            # 쫄을 만날 경우
            if board[nx][ny] == 1:
                if jumped: # 뛰어넘은 상태로 만난 쫄은 잡는 쫄 / 잡은 후 재탐색
                    catch.add((nx, ny)) # 잡은 좌표 추가
                    board[nx][ny] = 0 # 잡은 후 사라진 상태 처리
                    dfs(board, nx, ny, depth + 1) # 재탐색(이동 횟수 증가)
                    board[nx][ny] = 1 # (다른 경우의 수를 위하여 원상복귀)
                    break
                else: # 처음 마주하는 쫄은 뛰어넘어야 함
                    jumped = True
                    nx += dx
                    ny += dy
            # 빈 칸일 경우
            else:
                if jumped: # 뛰어넘은 상태로 모든 곳을 재탐색해야함
                    dfs(board, nx, ny, depth + 1)
                    nx += dx
                    ny += dy
                else: # 뛰어넘지 않은 상태의 공간은 무시(계속 나아감)
                    nx += dx
                    ny += dy
    return

T = int(input())
for t in range(T):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    catch = set() # 잡은 쫄의 좌표를 set에 추가해줘야 모든 경우의 수를 따져 중복되어 잡힌 쫄을 걸러낼 수 있음
    for i in range(N):
        for j in range(N):
            if board[i][j] == 2: # 포 위치 찾기
                board[i][j] = 0 # 포는 이동하니까 값 0으로 바꿔줘야 이동에 제약이 없음
                dfs(board, i, j, 1) # 탐색 시작
                break
    print(f"#{t + 1} {len(catch)}") # set의 길이 = 중복 제거한 잡은 쫄의 수
