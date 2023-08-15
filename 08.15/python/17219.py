import sys
input = sys.stdin.readline

N, M = map(int, input().split())

lst = dict()

for _ in range(N):
    adress, password = input().split()
    lst[adress] = password

result = []

for _ in range(M):
    find = input().strip()
    a = lst[find]
    result.append(a)

for i in result:
    print(i)