'''
영식 요금제(Y) = 30초마다 10원씩 청구
민식 요금제(M) = 60초마다 15원씩 청구

- 입력
이용한 통화의 개수 N <= 20
통화 시간 a, b, c, ...(N개) <= 10,000

- 출력
싼 요금제의 이름 + 공백 + 요금(두 요금제의 요금이 동일할 경우, Y M 순으로 출력)

'''

N = int(input())
times = list(map(int, input().split()))

Y, M = 0, 0

for i in times:
    Y += ((i // 30) + 1) * 10
    M += ((i // 60) + 1) * 15

if Y < M:
    print("Y", Y)
elif Y > M:
    print("M", M)
else:
    print("Y M", Y)