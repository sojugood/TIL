T = 10
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    total_list = []
    total_1 = total_2 = 0
    for i in range(100):
        total_1 += arr[i][i]
        total_2 += arr[i][99 - i]
    total_list.append(total_1)
    total_list.append(total_2)
    arr += [[arr[j][i] for j in range(100)] for i in range(100)]
    for i in range(200):
        total_3 = 0
        for j in range(100):
            total_3 += arr[i][j]
        total_list.append(total_3)
    total_list.sort(reverse=True)
    print(f"#{tc} {total_list[0]}")