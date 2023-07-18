'''
1번 데이터 -> 1번 컴퓨터 ... 10번 -> 10번 ... 11번 -> 1번 ...
데이터 개수 -> a ** b

입력
테스트 케이스의 개수 T
정수 a b
.
.
.
.

출력
각 테스트 케이스에 대해 마지막 데이터가 처리되는 컴퓨터 번호
'''
totals = []
T = int(input())

for _ in range(T):
    a, b = map(int, input().split())
    case = a ** b
    computer_num = (case % 10)
    totals.append(computer_num)

for total in totals:
    print(total)