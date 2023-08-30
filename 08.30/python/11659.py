import sys
input = sys.stdin.readline

N, M = map(int, input().split())

num_lst = list(map(int, input().split()))
sum_list = [0]
temp = 0
for i in range(N):
    temp += num_lst[i]
    sum_list.append(temp)

for _ in range(M):
    i, j = map(int, input().split())
    res = sum_list[j] - sum_list[i - 1]
    print(res)