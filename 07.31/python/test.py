N, M = map(int, input().split())

all_list = []
result_list = []
for _ in range(M):
    k_i = int(input())
    n = list(map(int, input().split()))
    all_list.append(n)
    while all_list:
        for i in range(N):
            if all_list[i][-1] == i + 1:
                result_list.append(i + 1)
                temp = all_list[i]
                temp.remove(i + 1)
    if len(result_list) == N:
        print('Yes')
    else:
        print('No')