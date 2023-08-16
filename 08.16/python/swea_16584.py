def f(i, N, s):
    global min_total
    if i == N:
        if s < min_total:
            min_total = s
        return
    elif s > min_total:
        return
    else:
        for j in range(i, N):
            P[i], P[j] = P[j], P[i]
            f(i + 1, N, s + arr[i][P[i]])
            P[i], P[j] = P[j], P[i]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    P = list(range(N))
    min_total = 101
    f(0, N, 0)
    print(f"#{tc} {min_total}")
