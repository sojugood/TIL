T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    queue = list(map(int, input().split()))
    count = 1
    temp = 0
    for i in range(0, M):
        if queue[i] == queue[M]:
            temp += 1
        elif queue[i] > queue[M]:
            temp = 0
            count += 1
    count += temp
    temp2 = 0
    check = 0
    for j in range(M + 1, N):
        if queue[j] == queue[M]:
            temp2 += 1
        elif queue[j] > queue[M]:
            temp2 = 0
            count += 1
            check += 1
    if check == 0:
        temp2 = 0
    count += temp2
    print(count)