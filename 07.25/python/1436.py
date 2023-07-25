N = input()

a = N + '666'

num_list = []

for i in range(666, int(a) + 1):
    if '666' in str(i):
        num_list.append(i)

print(num_list[int(N)-1])

'''
n = int(input())
i = 0
num = 665

while i < n:
    num += 1
    if '666' in str(num):
        i += 1

print(num)
'''