for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for j in range(N):
        temp = 0
        lst = []
        for i in range(N):
            if arr[i][j] != 0:
                lst.append(arr[i][j])
        for j in range(len(lst)):
            if lst[j] == 2:
                lst.pop(0)
            elif lst[j] == 1:
                break
        lst = lst[::-1]
        for j in range(len(lst)):
            if lst[j] == 1:
                lst.pop(0)
            elif lst[j] == 2:
                break
        for k in lst:
            if k != temp:
                cnt += 1
            temp = k
    print(cnt)