import sys
input = sys.stdin.readline

N, M = map(int, input().split())

N_lst = set()
M_lst = set()

for _ in range(N):
    N_name = input().strip()
    N_lst.add(N_name)
for _ in range(M):
    M_name = input().strip()
    M_lst.add(M_name)

result = N_lst & M_lst
result = list(result)
result.sort()
print(len(result))
for i in result:
    print(i)
