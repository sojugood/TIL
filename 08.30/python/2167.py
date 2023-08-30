import sys

input = sys.stdin.readline

N, M = map(int, input().split())

# Initialize array and prefix sum array
arr = [list(map(int, input().split())) for _ in range(N)]
prefix_sum = [[0] * (M + 1) for _ in range(N + 1)]

# Calculate 2D prefix sum
for i in range(1, N + 1):
    for j in range(1, M + 1):
        prefix_sum[i][j] = arr[i - 1][j - 1] + prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j - 1]

K = int(input())

for _ in range(K):
    i, j, x, y = map(int, input().split())
    
    # Using 2D prefix sum to get the sum of subarray
    res = prefix_sum[x][y] - prefix_sum[i - 1][y] - prefix_sum[x][j - 1] + prefix_sum[i - 1][j - 1]
    print(res)
