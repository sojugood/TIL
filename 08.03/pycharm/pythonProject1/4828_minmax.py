T = int(input())    # 테스트 케이스 수
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    max_v = arr[0]
    for v in arr[1:]:
        if v > max_v:
            max_v = v
    min_v = arr[0]
    for v in arr[1:]:
        if v < min_v:
            min_v = v
    ans = max_v - min_v

    print(f"#{tc} {ans}")