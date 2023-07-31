N, M = map(int, input().split())

for _ in range(M):
    k_i = int(input())
    n = list(map(int, input().split()))
    for i in range(1, k_i):
        if n[i] > n[i-1]:
            print('No')
            exit()
print('Yes')
