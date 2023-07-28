'''
연계 기술 : 사전 기술 -> 본 기술

하나의 사전 기술은 하나의 본 기술과만 연계해서 사용 가능
사전 기술만 사용 o
사전 기술 -> 다른 기술 -> 본 기술 o
본 기술만 사용 x

기술 목록
1 ~ 9, L -> R, S -> K

R 혹은 K 가 먼저 입력되어 있으면 이후 입력들은 처리 X
순서 L -> R, S - > K 만 정상적이면 O
L 혹은 S가 단독으로 사용되어도 무관, 카운트는 X
그 후, 숫자 카운트, 영어 카운트 후 출력
'''

N = int(input())
skill = input()

count = 0
L_count = 0
S_count = 0

for i in skill:
    if i == 'L':
        L_count += 1
    elif i == 'R':
        if L_count > 0:
            count += 1
            L_count -= 1
        else:
            break
    elif i == 'S':
        S_count += 1
    elif i == 'K':
        if S_count > 0:
            count += 1
            S_count -= 1
        else:
            break
    else:
        count += 1

print(count)