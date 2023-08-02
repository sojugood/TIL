numbers = range(1, 13)
T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    c = 0

    for i in range(1 << 12):  # 2^12의 조합을 만듦
        selected_numbers = []
        for j in range(12):
            if i & (1 << j):  # j번째 비트가 1인지 확인
                selected_numbers.append(numbers[j])

        if len(selected_numbers) == N and sum(selected_numbers) == K:
            c += 1

    print(f"#{test_case} {c}")