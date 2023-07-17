'''
컵 3개 1 2 3

공의 위치 기본 1번 컵

컵 위치 바꾸는 횟수 M

바꾸는 방법 X Y (X = Y 일 수 있다)

출력

공이 들어있는 컵의 위치 번호
'''

cups = [1, 2, 3]
M = int(input())

for _ in range(M):
    X, Y = list(map(int, input().split()))
    X, Y = X - 1, Y - 1  # 0부터 시작하는 인덱스를 만듭니다.
    cups[X], cups[Y] = cups[Y], cups[X]  # cups 리스트의 X번째 항목과 Y번째 항목을 교환합니다.

print(cups.index(1) + 1)
