from collections import deque
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    time_lst = [0]
    connect = [[] for _ in range(N + 1)]
    result = float("inf")
    flag = 1
    for i in range(N):
        info = list(map(int, input().split()))
        time_lst.append(info[0])
        if info[1] == 0:
            connect[i + 1].append(-1)
        else:
            for j in range(2, len(info)):
                connect[i + 1].append(info[j])

    for v in range(1, N + 1):
        cop = [row[:] for row in connect]
        origin = time_lst[v]
        time_lst[v] //= 2
        lst = []
        res_lst = [[] for _ in range(N + 1)]
        check = N
        for i in range(1, N + 1):
            if -1 in cop[i]:
                lst.append((time_lst[i], i))
                res_lst[i].append(time_lst[i])
                check -= 1
        lst = sorted(lst)
        q = deque(lst)
        while check > 0:
            if not q:
                flag = 0
                break
            q = deque(sorted(q))
            t, idx = q.popleft()
            temp = []
            for l in range(1, N + 1):
                if idx in cop[l]:
                    cop[l].remove(idx)
                if not cop[l]:
                    temp.append(time_lst[l] + t)
                    cop[l].append(-1)
                    check -= 1
                    q.append((time_lst[l] + t, l))
            if temp:
                if res_lst[idx]:
                    if max(temp) > res_lst[idx][0]:
                        res_lst[idx] = [max(temp)]
                    else:
                        pass
                else:
                    res_lst[idx].append(max(temp))
        res = max(sum(row) for row in res_lst)
        result = min(result, res)
        time_lst[v] = origin
        if flag == 0:
            result = -1
            break
    print(f"#{tc} {result}")