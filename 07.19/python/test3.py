T = int(input())

result = []

for i in range(T):
    num = int(input())
    score = input().split() # 바로 list로 가능(int 필요없을 때)
    count = {} # 중복 횟수 세기 - dict
    for j in score:
        if j in count:
            count[j] += 1 # 키 - 값 추가
        else:
            count[j] = 1
    max_value = max(list(count.values())) # 가장 많이 중복된 횟수
    max_keys = [k for k, l in count.items() if l == max_value] # 가장 많이 중복된 횟수와 일치하는 숫자 값
    F = num, max(max_keys) # 숫자 값 중 가장 큰 값(중복 횟수의 중복 시 더 큰 수를 출력)
    result.append(F)


for a, b in result:
    print(f'#{a} {b}')