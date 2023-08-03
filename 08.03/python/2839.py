N = int(input())
remainder = [0, 2, 4, 1, 3]
count_3 = remainder[N % 5]
count_5 = (N - (3 * count_3)) // 5
if count_5 >= 0:
    print(count_3 + count_5)
else:
    print(-1)