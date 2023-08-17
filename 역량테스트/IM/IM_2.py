T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_size = 0
    count = 0
    for i in range(N):
        for j in range(N):
            for k in range(i, N):
                potential_size = (N - i) * (N - j)  # 최대 가능한 크기 계산
                if potential_size < max_size:
                    break
                for l in range(j, N):
                    if arr[i][j] == arr[k][l]:
                        size = (k - i + 1) * (l - j + 1)
                        if size > max_size:
                            max_size = size
                            count = 1
                        elif size == max_size:
                            count += 1
    print(f"#{tc} {count}")
