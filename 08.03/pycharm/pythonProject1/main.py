T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    num = 1
    for s in range((N + 1) // 2):
        for i in range(s, N - s):
            arr[s][i] = num
            num += 1
        for j in range(s + 1, N - s):
            arr[j][N - s - 1] = num
            num += 1
        for k in range(N - s - 2, s - 1, -1):
            arr[N - s -1][k] = num
            num += 1
        for l in range(N - s - 2, s, -1):
            arr[l][s] = num
            num += 1
    print(f"#{tc}")
    for r in arr:
        print(*r)