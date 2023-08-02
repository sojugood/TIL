T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    kill_list = []
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            s = 0
            for k in range(i, i + M):
                for l in range(j, j + M):
                    s += arr[k][l]
            kill_list.append(s)
    kill_list.sort(reverse=True)
    print(f"#{tc} {kill_list[0]}")