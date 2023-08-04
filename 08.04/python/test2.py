T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    input_Arr = [list(map(int, input().split())) for _ in range(N)]
    result_list = []

    for _ in range(3):
        input_Arr = list(zip(*input_Arr[::-1]))
        for i in input_Arr:
            result_list.append(''.join(map(str, i)))
    print(f"#{test_case}")
    for i in range(0, N):
        print(f"{result_list[i]} {result_list[i + N]} {result_list[i + 2 * N]}")