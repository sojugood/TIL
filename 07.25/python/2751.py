import sys
input = sys.stdin.readline

N = int(input())

num_list = []

for _ in range(N):
    n = int(input())
    num_list.append(n)

num_list.sort()

for i in num_list:
    print(i)