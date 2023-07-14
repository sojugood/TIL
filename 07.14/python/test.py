from turtle import *

shape('turtle')

# 원의 반지름
r = 100



from random import randrange

import math

def in_circle(x, y, r):
    return math.sqrt(x ** 2 + y ** 2) <= r

def draw_random_dot():
    x, y = randrange(-r, r), randrange(-r, r)
    goto(x, y)
    if in_circle(x, y, r):
        color('red')  # 원 안에 있으면 빨간색 점
    else:
        color('blue')  # 원 밖에 있으면 파란색 점
    dot()


# 재설정
reset()

# r만큼 이동해서 그리기 준비
up(); forward(r); down(); left(90)

# 반지름이 r인 원 그리기
circle(r)

# 한 변의 길이가 r의 두 배인 정사각형 그리기
for i in range(4):
    forward(r); left(90); forward(r)

# 자취를 남기지 않기
penup()

# 점 30개 찍기
for i in range(30):
    draw_random_dot()

# 거북이 숨기기
hideturtle()