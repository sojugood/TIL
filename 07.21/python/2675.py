T = int(input())

total_list = []

for i in range(T):
    R, S = input().split()
    R = int(R)
    S = list(S)
    print_list = []
    for i in range(len(S)):
        print_list.append(S[i] * R)
    total_list.append(print_list)

for i in total_list:
    print(''.join(i))

'''
T = int(input())
for i in range(T):
    R, S = input().split()
    R = int(R)
    for i in S:
        print(i * R, end = "")
    print()
'''