import sys

results = []

for j in range(3):
    n = int(sys.stdin.readline().rstrip()) # input() 함수는 입/출력 속도가 상대적으로 느린 편이라, 대량의 데이터를 입력받아야 할 때에는 sys.stdin.readline() 함수를 사용하는 것이 더 빠름. 대신 이 함수는 문자열의 끝에 있는 줄 바꿈 문자('\n')를 포함하여 읽어오기 때문에 rstrip() 함수를 사용하여 문자열의 오른쪽 끝에 있는 ('\n')을 제거하여야 값을 정수로 받아올 수 있음.
    sum = 0

    for i in range(n):
        num = int(sys.stdin.readline().rstrip())
        sum = sum + num

    if sum == 0:
        results.append('0')
    elif sum > 0:
        results.append('+')
    elif sum < 0:
        results.append('-')

for result in results:
    print(result)