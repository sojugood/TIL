Start_B = 'BWBWBWBWWBWBWBWB' * 4
Start_W = 'WBWBWBWBBWBWBWBW' * 4

N, M = map(int, input().split())

chess = [list(input()) for _ in range(N)]

count = 65
for i in range(N - 8 + 1):
    for j in range(M - 8 + 1):
        pattern = ''
        count1 = 0
        count2 = 0
        for k in range(i, i + 8):
            for l in range(j, j + 8):
                pattern += chess[k][l]
        for idx in range(64):
            if pattern[idx] != Start_B[idx]:
                count1 += 1
            if pattern[idx] != Start_W[idx]:
                count2 += 1
        if count1 == count2 and count1 < count:
            count = count1
        elif count1 < count and count1 < count2:
            count = count1
        elif count2 < count and count2 < count1:
            count = count2
print(count)