T = 10
for tc in range(1, T + 1):
    N = int(input())
    arr = [[0] + list(map(int, input().split())) + [0] for _ in range(100)][::-1]
    for i in range(102):
        if arr[0][i] == 2:
            start = i
    row = 1
    col = start
    while row < 100:
        if arr[row][col + 1] == 1:
            col += 1
            while True:
                col += 1
                if arr[row + 1][col] == 1:
                    break
        elif arr[row][col - 1] == 1:
            col -= 1
            while True:
                col -= 1
                if arr[row + 1][col] == 1:
                    break
        row += 1
    print(f"#{tc} {col - 1}")