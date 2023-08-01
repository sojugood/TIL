n = input()

count = [0] * 10
for i in n:
    if i == '9':
        count[6] += 1
    else:
        count[int(i)] += 1

if count[6] % 2 == 0:
    count[6] = count[6] // 2
else:
    count[6] = (count[6] // 2) + 1

count.sort(reverse=True)

print(count[0])