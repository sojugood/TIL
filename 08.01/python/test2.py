T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    N_list = []
    for _ in range(N):
        A, B = map(int, input().split())
        N_list.extend(list(range(A, B + 1)))
    P = int(input())
    count = [0] * P
    for j in range(P):
        C = int(input())
        for i in N_list:
            if i == C:
                count[j] += 1
    print(f"#{test_case}", *count)