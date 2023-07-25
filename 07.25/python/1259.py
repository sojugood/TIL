while True:
    n = input()
    if n == '0':  # 입력이 "0"인 경우 루프를 종료
        break
    n_list = list(n)
    n_revers = list(reversed(n))
    if n_list == n_revers:
        print('yes')
    else:
        print('no')
