def dfs(arr, i, j):
    arr[i][j] = ' '
    if i+1 < len(arr) and arr[i+1][j] == '|':
        dfs(arr, i+1, j)
    # else:
    #     return
N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
cnt = 0
for i in range(N):
    tmp = 0
    for j in range(M):
        if arr[i][j] == '-':
            if tmp == 0:
                cnt += 1
                tmp = 1
            else:
                continue
        elif arr[i][j] == '|':
            tmp = 0
            cnt += 1
            dfs(arr, i, j)
        else:
            tmp = 0
print(cnt)