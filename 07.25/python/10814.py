import sys
input = sys.stdin.readline

N = int(input())

data_list = []

for _ in range(N):
    data = list(input().split())
    data_list.append(data)

data_list.sort(key=lambda x: int(x[0])) # age를 int로 바꿔줘야함

for i in data_list:
    print(*i)