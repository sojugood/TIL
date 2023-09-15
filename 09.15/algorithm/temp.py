def solution(n, l, r):
    answer = 0
    dp = ['1']*21
    for i in range(1, n + 1):
        tmp = ''
        for j in dp[i - 1]:
            if j == '1':
                tmp += '11011'
            else:
                tmp += '00000'
        dp[i] = tmp
    answer = dp[n][l-1:r]
    return answer

print(solution(2,4,17))