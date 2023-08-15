N = int(input())

dp = [0, 0, 1, 1]

if N >= 4:
    for i in range(4, N + 1):
        tmp1 = 1 + dp[i - 1]
        tmp2 = tmp1
        tmp3 = tmp1

        if i % 2 == 0:
            tmp2 = 1 + dp[i // 2]

        if i % 3 == 0:
            tmp3 = 1 + dp[i // 3]
        
        dp.append(min(tmp1, tmp2, tmp3))

print(dp[N])