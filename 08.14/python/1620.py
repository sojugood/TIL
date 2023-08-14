import sys
input = sys.stdin.readline

N, M = map(int, input().split())

lst = dict()
for i in range(N):
    a = input().strip()
    lst[a] = i + 1
    lst[i + 1] = a

for _ in range(M):
    b = input().strip()
    try:
        print(lst[int(b)])
    except ValueError:
        print(lst[b])
