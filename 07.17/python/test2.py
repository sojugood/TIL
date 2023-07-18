<<<<<<< HEAD
totals = []
T = int(input())

for _ in range(T):
    a, b = map(int, input().split())
    last_digit = a % 10  # a의 일의 자리 숫자

    if last_digit in (1, 5, 6):
        result = last_digit
    elif last_digit == 0:
        result = 10
    elif last_digit in (4, 9):
        result = pow(last_digit, b % 2 + 4) % 10
    else:
        result = pow(last_digit, b % 4 + 4) % 10

    totals.append(result)

for total in totals:
    print(total)
=======
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
>>>>>>> 6392f4a56288ba59e3de35a27ee8a35405712f1b
