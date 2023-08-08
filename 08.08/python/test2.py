N = int(input())
arr = [[0] * 100 for _ in range(100)]
count = 0
for _ in range(N):
    x, y = map(int, input().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            if arr[i][j] == 0:
                count += 1
                arr[i][j] = 1
print(count)
