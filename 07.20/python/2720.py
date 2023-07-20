'''
거스름돈 <= 5.00

동전
0.25
0.10
0.05
0.01

ex) 1.24 = 0.25 * 4 + 0.10 * 2 + 0.05 * 0 + 0.01 * 4


'''
from decimal import Decimal

Q = Decimal('0.25')
D = Decimal('0.10')
N = Decimal('0.05')
P = Decimal('0.01')

coin_list = [Q, D, N, P]
print_list = []

T = int(input())

for i in range(T):
    C = int(input())
    S = Decimal(C) / 100
    value_list = []
    for j in coin_list:
        value = int(S // j)
        value_list.append(value)
        S = S % j
    print_list.append(value_list)

for k in print_list:
    print(*k)

