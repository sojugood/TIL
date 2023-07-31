T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    
    result = N - 1
    for i in arr[1:]:
        if i >= arr[0]:
            result -= 1
    print(f"#{test_case} {result}")