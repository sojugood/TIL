def div(N):
    for i in range(0, N-1, 2):
        for j in range(0, N-1, 2):
            tmp = []
            tmp.append(arr[i][j])
            tmp.append(arr[i][j + 1])
            tmp.append(arr[i + 1][j])
            tmp.append(arr[i + 1][j + 1])
            tmp.sort()
            res.append(tmp[1])

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

res = []

if N > 2:
    div(N)
    res.sort()
    print(res[1])

else:
    if N == 1:
        print([row[0] for row in arr][0])
    else:
        temp = []
        for i in range(N):
            for j in range(N):
                temp.append(arr[i][j])
        temp.sort()
        print(temp[1])