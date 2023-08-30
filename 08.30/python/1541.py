expression = input().split('-')
min_value = 0

# 첫 번째 항에 대한 처리
first_term = list(map(int, expression[0].split('+')))
min_value += sum(first_term)

# 나머지 항에 대한 처리
for term in expression[1:]:
    numbers = list(map(int, term.split('+')))
    min_value -= sum(numbers)

print(min_value)
