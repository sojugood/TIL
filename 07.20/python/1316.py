import re

N = int(input())

result = 0

for i in range(N):
    word = input()
    word = re.sub(r"([a-z])\1*", r"\1", word) # \1* : 같은 문자가 하나 이상 연속으로 나오는 부분을 의미
    if len(word) == len(set(word)):
        result += 1
    else:
        result += 0

print(result)