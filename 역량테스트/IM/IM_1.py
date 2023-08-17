di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
T = int(input())

for tc in range(1, T + 1):
    N, P = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_bomb = 0
    for i in range(N):
        for j in range(N):
            bomb = arr[i][j]
            for k in range(4):
                for p in range(1, P + 1):
                    ni, nj = i + di[k]*p, j + dj[k]*p
                    if 0 <= ni < N and 0 <= nj < N:
                        bomb += arr[ni][nj]
            if max_bomb < bomb:
                max_bomb = bomb
    print(f"#{tc} {max_bomb}")