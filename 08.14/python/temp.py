N, K = map(int, input().split())

val_lst = [int(input()) for _ in range(N)]

val_lst = sorted(val_lst, reverse=True)

count = 0

for i in val_lst:
    if K - i >= 0:
        while True:
            if K - i >= 0:
                K = K - i
                count += 1
            else:
                break
print(count)
