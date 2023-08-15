import sys
input = sys.stdin.readline

N, K = map(int, input().split())

val_lst = [int(input()) for _ in range(N)]

val_lst = sorted(val_lst, reverse=True)

count = 0

for i in val_lst:
    if K - i >= 0:
        count += K // i
        K = K % i
    if K == 0:
        break
print(count)
