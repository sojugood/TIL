totals = []

while True:
    num = int(input())

    if num == 0:
        break

    digits = []
    while num > 0:
        digits.append(num % 10)
        num = num // 10
    digits.reverse()  # 숫자를 원래 순서로 뒤집습니다.

    total = 2
    for i in digits:
        if i == 1:
            cm = 3
        elif i == 0:
            cm = 5
        else:
            cm = 4
        total += cm
    total = total - 1
    totals.append(total)

for total in totals:
    print(total)