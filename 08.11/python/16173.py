direction = [(1, 0), (0, 1)]

def dfs(i, j, arr):
    k = arr[i][j]
    if k == -1:
        return 'HaruHaru'
    elif k >= len(arr) or k == 0:
        return 'Hing'
    
    for dx, dy in direction:
        ni, nj = i + dx*k, j + dy*k
        if 0 <= ni < len(arr) and 0 <= nj < len(arr):
            result = dfs(ni, nj, arr)
            if result == 'HaruHaru':
                return 'HaruHaru'
    return 'Hing'

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
result = dfs(0, 0, arr)
print(result)