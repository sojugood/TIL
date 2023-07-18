''' 문제(나누기)
정수 N, F

N의 가장 뒤 두 자리를 바꿔서 N // F = 0 으로 만든다
(가능한 것 중 뒤 두 자리가 가장 작게)

ex)
N = 275, F = 5 이면 답은 00 -> 200 // 5 = 0 이기 때문
N = 1021, F = 11 이면 답은 01 -> 1001 // 11 = 0 이기 때문

입력
N(>= 100)
F(< 100)

출력
바꾼 두 자리(한 자리이면 앞에 0 추가)
'''

''' 쉬운 코드
N = int(input())
F = int(input())

N = (N // 100) * 100  # 마지막 두 자리를 0으로 만듭니다.

while N % F != 0:  # N이 F로 나누어 떨어질 때까지
    N += 1  # N을 1씩 증가시킵니다.

print(str(N)[-2:].zfill(2))  # 마지막 두 자리를 출력합니다. zfill 함수를 이용하여 0으로 패딩합니다.
'''

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
