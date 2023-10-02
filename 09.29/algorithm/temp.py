def per(k, d, lis):
    if d == M:
        res.add(tuple(lis))
        return
    
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            per(k + 1, d + 1, lis + [lst[i]])
            visited[i] = 0

N, M = map(int, input().split())

lst = list(map(int, input().split()))
lst.sort()

visited = [0] * N

res = set()

per(0, 0, [])

res = list(res)
res.sort()

for i in res:
    print(*i)