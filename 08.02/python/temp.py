T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    real_count = 0

    for i in range(N):
        count = 0
        for j in range(N):
            if arr[i][j] == 1:
                count += 1
            else:
                if count == K:
                    real_count +=1
                count = 0
        if count == K:
            real_count += 1

    for i in range(N):
        count = 0
        for j in range(N):
            if arr[j][i] == 1:
                count += 1
            else:
                if count == K:
                    real_count += 1
                count = 0
        if count == K:
            real_count += 1

    print(f"#{tc} {real_count}")
