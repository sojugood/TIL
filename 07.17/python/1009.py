totals = []
T = int(input())

for _ in range(T):
    a, b = map(int, input().split())
    last_digit = a % 10  # a의 일의 자리 숫자

    if last_digit in (1, 5, 6):
        result = last_digit
    elif last_digit == 0:
        result = 10
    elif last_digit in (4, 9):
        result = pow(last_digit, b % 2 + 4) % 10
    else:
        result = pow(last_digit, b % 4 + 4) % 10

    totals.append(result)

for total in totals:
    print(total)
