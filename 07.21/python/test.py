T = int(input())

for i in range(T):
    R, S = input().split()
    R = int(R)
    S = list(S)
    print_list = []
    for i in range(len(S)):
        print_list.append(S[i])