T = int(input())

for tc in range(1, T + 1):
    N, K = map(int,input().split())
    Sample = list(map(int,input().split()))
    PassCode = list(map(int,input().split()))
    i = 0
    count = 0
    for _ in range(K):
        while i < N:
            if PassCode[_] == Sample[i]:
                i += 1
                count += 1
                break
            else:
                i += 1
    if count == K:
        print(f"#{tc} 1")
    else:
        print(f"#{tc} 0")