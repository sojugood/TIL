# T = int(input())

# for test_case in range(1, T + 1):
#     K, N, M = map(int, input().split())
#     charge = list(map(int, input().split()))
#     count = 0
#     charge_list = [0] * (N + 1)
#     for i in charge:
#         charge_list[i] += 1
#     for i in range(K, N + 1, K):
#         if 1 in charge_list[(i - K) + 1 : i + 1]:
#             count += 1
#         else:
#             count = 0
#             break

#     print(f"#{test_case} {count}")
T = int(input())

for test_case in range(1, T + 1):
    K, N, M = map(int, input().split())
    charge = list(map(int, input().split()))
    charge_list = [0] * (N + 1)
    for i in charge:
        charge_list[i] = 1

    count = 0
    current_position = 0
    success = False  # 종점에 도착했는지 확인하는 플래그

    while True:
        for i in range(current_position + K, current_position, -1):
            if i >= N:  # 종점 도착
                print(f"#{test_case} {count}")
                success = True
                break
            if charge_list[i] == 1:  # 충전소 발견
                count += 1
                current_position = i
                break
        # 충전소를 찾지 못한 경우의 처리
        else:  
            print(f"#{test_case} 0")
            break
        if success:  # 종점에 도착했다면 while 루프 빠져나오기
            break

