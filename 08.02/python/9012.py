T = int(input())

for i in range(T):
    n = input()
    while True:
        new_n = n
        n = n.replace("()", "")
        if n == new_n:
            print('NO')
            break
        elif len(n) == 0:
            print('YES')
            break