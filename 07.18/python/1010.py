'''
nCr
'''

from math import factorial as fct
T = int(input())

result_list = []

for _ in range(T):
    N, M = map(int, input().split())
    C = fct(M) // (fct(M - N) * fct(N))
    result_list.append(C)

for C in result_list:
    print(C)