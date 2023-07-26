import sys
input = sys.stdin.readline

N = int(input())

num_list = []

for i in range(N):
    n = map(int, input().split())
    xy_list = list(n)
    num_list.append(xy_list)

num_list.sort(key=lambda x: (x[0], x[1]))

for i in num_list:
    print(*i)