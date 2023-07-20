'''
1
    6
7
    12
19
    18
37
    24
61

13 // 6 = 2
'''

N = int(input())

Start = 1
i = 1
while True:
    if N <= Start:
        print(i)
        break
    Start += i * 6
    i += 1