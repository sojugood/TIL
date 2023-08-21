T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    
    tree = [[] for _ in range(N + 1)]

    for i in range(1, N):
        tree[i].append(i + 1*i)
        tree[i].append(2*i + 1)

    lst = [0] * (N + 1)

    for i in range(2, N + 1):
        lst[i] = i // 2


        cnt = 0
        i = 1
        while True:
            ch1[i].append(2 * i)
            cnt += 1
            if cnt == N:
                break
            ch2[i].append(2 * i + 1)
            cnt += 1
            if cnt == N:
                break
            i += 1