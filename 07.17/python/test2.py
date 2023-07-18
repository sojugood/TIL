N = str(int(input()))
F = int(input())

a = list(N)

a[-2:] = [0, 0]

a_list = [str(i) for i in a]
a_str = ''.join(a_list)
a = int(a_str)

if a % F == 0:
    c = '00'
    print(c)
else:
    m = (a // F) + 1 # 몫
    a_new = m * F # 뒤 두자리 바뀐 a값
    a_new_list = list(str(a_new))
    a_new_list_last2 = a_new_list[-2:]
    A_list = [str(j) for j in a_new_list_last2]
    A_str = ''.join(A_list)
    A = int(A_str)
    if A < 10:
        print(f'0{A}')
    else:
        print(A)
