import sys
input = sys.stdin.readline

N = int(input())

lst = list(map(int, input().split()))

lst_sort = sorted(list(set(lst)))

idx_dict = {num: idx for idx, num in enumerate(lst_sort)}

for n in lst:
    print(idx_dict[n], end=' ')