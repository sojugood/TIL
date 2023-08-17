T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    Ci = list(map(int, input().split()))
    queue = []
    Idx_lst = list(range(1, N + 1))
    Idx = N
    for i in range(N):
        temp = Ci.pop(0)
        queue.append(temp)
    while True:
        if len(queue) == 1:
            break
        queue[0] = queue[0] // 2
        temp = queue.pop(0)
        temp_Idx = Idx_lst.pop(0)
        if temp == 0:
            if Ci:
                temp = Ci.pop(0)
                Idx += 1
                temp_Idx = Idx
            else:
                continue
        queue.append(temp)
        Idx_lst.append(temp_Idx)
    print(f"#{tc}", *Idx_lst)