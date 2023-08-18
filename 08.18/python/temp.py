direction_1 = [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (-1, 1)]
direction_2 = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (1, 1)]

def dfs(arr, i, j, depth, v):
    if depth == 4:
        total.append(v)
        return
    arr[i][j] = 0
    if j % 2 == 0:
        for dx, dy in direction_1:
            ni, nj = i + dx, j + dy
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] != 0:
                v += arr[ni][nj]
                dfs(arr, ni, nj, depth + 1, v)
                
    elif j % 2 == 1:
        for dx, dy in direction_2:
            ni, nj = i + dx, j + dy
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] != 0:
                v += arr[ni][nj]
                dfs(arr, ni, nj, depth + 1, v)
