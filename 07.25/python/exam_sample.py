# case 1
# scores의 평균 구하기
# 단, len, sum 사용 X
# sol

scores = [85, 90, 100]

count = 0
sum = 0
for i in scores:
    count += 1
    sum += i

result = sum / count
print(result)


# case 2
# numbers 리스트의 최소 최댓값 호출
# min, max 사용 X
# sol
'''

최소, 최댓값으로 임의의 리스트 값 설정
for 문 -> 설정값과 리스트 값 비교(if 문) -> 최소, 최댓값 다시 설정
return

'''


# case 3
# 5-1 실습
# result = ''
# result = char + result