T = 10

for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    result = 0
    for i in range(2, N - 2):
        if arr[i] > arr[i - 1] and arr[i] > arr[i - 2] and arr[i] > arr[i + 1] and arr[i] > arr[i + 2]:
            left_list = []
            right_list = []
            left_list.extend([arr[i - 1], arr[i - 2]])
            left_list.sort(reverse=True)
            right_list.extend([arr[i + 1], arr[i + 2]])
            right_list.sort(reverse=True)
            case_1 = arr[i] - left_list[0]
            case_2 = arr[i] - right_list[0]
            if case_1 > case_2:
                result += case_2
            elif case_2 > case_1:
                result += case_1
            elif case_1 == case_2:
                result += case_1
    print(f"#{test_case} {result}")