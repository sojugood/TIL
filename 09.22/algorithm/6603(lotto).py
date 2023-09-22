import sys
input = sys.stdin.readline

def dfs(start, depth):
    if depth == 6:
        tmp = []
        for i in range(6):
            tmp.append(number_lst[i])
        print(*tmp)
        return

    for i in range(start, k):
        number_lst[depth] = lst[i + 1]
        dfs(i + 1, depth + 1)

while True:
    lst = list(map(int, input().split()))
    if lst[0] == 0:
        break
    else:
        k = lst[0]

    number_lst = [0] * k
    dfs(0, 0)
    print()