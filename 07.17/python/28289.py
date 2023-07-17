'''
2학년부터 동아리 가능

1, 2반 -> 소프트웨어 개발과
3반 -> 임베디드소프트웨어 개발과
4반 -> 인공지능소프트웨어 개발과


입력
5 <- 학생수 P
1 3 5 <- 학년 반 번호
2 1 10 <- 학년 반 번호
.
.
.

출력
1. 동아리 소속 소프트웨어 개발과 학생 수
2. 동아리 소속 임베디드소프트웨어 개발과 학생 수
3. 동아리 소속 인공지능소프트웨어 개발과 학생 수
4. 동아리 소속되지 않은 1학년 학생 수

sol)
학년 >= 2 이면 반으로 구분하여 1 2 3 에 출력
학년 == 1이면 4에 출력
'''

result_1 = []
result_2 = []
result_3 = []
result_4 = []

P = int(input())

for _ in range(P):
    G, C, N = map(int, input().split())
    if G >= 2:
        if C == 1 or C == 2:
            r1 = 1
            result_1.append(r1)
        elif C == 3:
            r2 = 1
            result_2.append(r2)
        elif C == 4:
            r3 = 1
            result_3.append(r3)
    else:
        r4 = 1
        result_4.append(r4)

print(len(result_1))
print(len(result_2))
print(len(result_3))
print(len(result_4))
