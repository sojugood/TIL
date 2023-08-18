def f(i):
    if i == N:
        return
    global cnt
    for j in range(0, N):
        if arr[j][0] > arr[i][-1]:
            break
    else:
        cnt += 1
    f(i + 1)
 
T = int(input())
 
for tc in range(1, T + 1):
    N = int(input())
    arr = [sorted(list(map(int, input().split()))) for _ in range(N)]
    cnt = 1
    f(0)
    print(f"#{tc} {cnt}")