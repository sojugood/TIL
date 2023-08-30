N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

res0 = 0
res1 = 0

S = N
while True:
    for i in range(0, N, S):
        for j in range(0, N, S):
            temp0 = 0
            lst0 = []
            temp1 = 0
            lst1 = []
            for k in range(i, i + S):
                for l in range(j, j + S):
                    if arr[k][l] == 0:
                        lst0.append((k, l))
                        temp0 += 1
                    elif arr[k][l] == 1:
                        lst1.append((k, l))
                        temp1 += 1
            if temp0 == S * S:
                for x, y in lst0:
                    arr[x][y] = 2
                res0 += 1
            if temp1 == S * S:
                for x, y in lst1:
                    arr[x][y] = 2
                res1 += 1
    if sum(sum(row) for row in arr) == 2 * N * N:
        break
    else:
        S //= 2

print(res0)
print(res1)
