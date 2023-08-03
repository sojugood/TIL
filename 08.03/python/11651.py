import sys
input = sys.stdin.readline

N = int(input())

dot_list = []
for _ in range(N):
    xy = list(map(int, input().split()))
    dot_list.append(xy)

dot_list.sort(key = lambda x : (x[1], x[0]))

for i in dot_list:
    print(*i)