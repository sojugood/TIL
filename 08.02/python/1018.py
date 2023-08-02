case1 = ('WB' * 4 + 'BW' * 4) * 4
case2 = ('BW' * 4 + 'WB' * 4) * 4

N, M = map(int, input().split())
arr = [input().strip() for _ in range(N)]

count = []

for i in range(N - 8 + 1):
    for j in range(M - 8 + 1):
        s = ''
        for k in range(i, i + 8):
            for l in range(j, j + 8):
                s += arr[k][l]

        diff_count1 = 0
        diff_count2 = 0
        for idx in range(64):
            if case1[idx] != s[idx]:
                diff_count1 += 1
            if case2[idx] != s[idx]:
                diff_count2 += 1

        count.append(diff_count1)
        count.append(diff_count2)

print(min(count))
