'''
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
<<<<<<< HEAD
totals = []
T = int(input())

for _ in range(T):
    a, b = map(int, input().split())
    case = a ** b
    computer_num = (case % 10)
    totals.append(computer_num)
=======
N = int(input())
F = int(input())

N = (N // 100) * 100  # 마지막 두 자리를 0으로 만듭니다.
>>>>>>> 6392f4a56288ba59e3de35a27ee8a35405712f1b

while N % F != 0:  # N이 F로 나누어 떨어질 때까지
    N += 1  # N을 1씩 증가시킵니다.

print(str(N)[-2:].zfill(2))  # 마지막 두 자리를 출력합니다. zfill 함수를 이용하여 0으로 패딩합니다.
