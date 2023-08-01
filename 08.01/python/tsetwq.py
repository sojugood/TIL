T = int(input())
for test_case in range(1,T+1):
    K,N,M = map(int,input().split())
    charge_lst = list(map(int,input().split()))
    charge_lst.sort()
    is_valid = True

    charge_lst.insert(0, 0) #charge_lst간 거리 파악을 위해 0,N 처음,끝 추가
    charge_lst.append(N)

    for i in range(M+1): #도착 불가 경우 판독
        if charge_lst[i+1] - charge_lst[i] > K:
            is_valid = False
            print(f'#{test_case} 0')
            break
    
    s_list = [K * s for s in range(1, (N//K) + 1)]

    if is_valid: #도착 가능의 경우 최소 충전횟수 출력
        if K >= N:
            print(f'#{test_case} 0')

        else:
            if N % K == 0 and all(element in charge_lst for element in s_list):
                print(f'#{test_case} {N//K - 1}')
            else:
                print(f'#{test_case} {N//K}')