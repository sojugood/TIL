T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())
    zero_list = [1] * n
    for _ in range(k):
        for i in range(n):
            if (i < n - 1):
                zero_list[i] = sum(zero_list[i:n])
    print(sum(zero_list))