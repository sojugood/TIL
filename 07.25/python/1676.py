from math import factorial as fac

N = int(input())

num_str = str(fac(N))

rev_num_str = ''.join(reversed(num_str))

count = 0

for i in rev_num_str:
    if i == '0':
        count += 1
    else:
        print(count)
        break