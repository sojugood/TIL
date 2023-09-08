def dfs(start, N, M, path):
    global res
    if M == 0:
        tmp = ''
        for i in path:
            tmp += str(i)
        res.append(tmp)
        return
    for i in range(start, N+1):
        dfs(i+1, N, M-1, path + [i])

N, M = map(int, input().split())
dfs(1, N, M, [])

res = []

print(res)