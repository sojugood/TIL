def per(k, d, lis):
    if k == M:
        print(*lis)
        return
    
    for i in range(d, N):
        per(k + 1, i, lis + [lst[i]])

N, M = map(int, input().split())

lst = list(map(int, input().split()))
lst.sort()

per(0, 0, [])