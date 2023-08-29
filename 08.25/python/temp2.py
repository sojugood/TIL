import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

K = int(input())

for _ in range(K):
    i, j, x, y = map(int, input().split())
    res = 0
    for k in range(i - 1, x):
        for l in range(j - 1, y):
            res += arr[k][l]
    print(res)