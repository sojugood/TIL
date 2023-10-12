from collections import deque

def bfs(g):
    q = deque([])
    visited = [0] * N
    visited[g[0]] = 1
    q.append(g[0])
    cnt = 1
    while q:
        next = q.popleft()
        for end in lst[next]:
            if end in g and not visited[end]:
                visited[end] = 1
                q.append(end)
                cnt += 1
    if cnt == len(g):
        return True
    return False


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    people = list(map(int, input().split()))
    lst = [[] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                lst[i].append(j)

    result = float("inf")

    for i in range(1, 1 << N - 1):
        group1 = [j for j in range(N) if i & 1 << j]
        group2 = [j for j in range(N) if not i & 1 << j]
        if bfs(group1) and bfs(group2):
            diff = abs(sum(people[i] for i in group1) - sum(people[i] for i in group2))
            result = min(result, diff)

    print(f"#{tc} {result}")