N = input()
num = set(input().split())

M = input()
num_2 = input().split()

for i in num_2:
    if i in num:
        print(1, end=' ')
    else:
        print(0, end=' ')