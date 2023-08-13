def dfs(matrix, start, end, visited):
    if start == end:
        return True

    visited[start] = True
    for i in range(len(matrix)):
        if matrix[start][i] == 1 and not visited[i]:
            if dfs(matrix, i, end, visited):
                return True
    return False

T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    matrix = [[0] * (V + 1) for _ in range(V + 1)]

    for _ in range(E):
        u, v = map(int, input().split())
        matrix[u][v] = 1

    S, G = map(int, input().split())
    visited = [False] * (V + 1)

    if dfs(matrix, S, G, visited):
        print(1)
    else:
        print(0)