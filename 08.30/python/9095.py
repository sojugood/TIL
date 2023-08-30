T = int(input())

for _ in range(T):
    n = int(input())
    dp = [1, 2, 4]
    for i in range(3, n):
        d = dp[i - 1] + dp[i - 2] + dp[i - 3]
        dp.append(d)
    print(dp[n-1])