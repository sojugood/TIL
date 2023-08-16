N = int(input())

score = [0] + [int(input()) for _ in range(N)]

if N == 1:
    print(score[1])
    exit()

dp = [[0, 0, 0] for _ in range(N + 1)]

dp[1][1] = score[1]
dp[1][2] = 0
dp[2][1] = score[2]
dp[2][2] = score[1] + score[2]

for i in range(3, N + 1):
    dp[i][1] = max(dp[i - 2][1], dp[i - 2][2]) + score[i]
    dp[i][2] = dp[i - 1][1] + score[i]

print(max(dp[N]))