N = int(input())

people_list = []

for _ in range(N):
    n = int(input())
    people_list.append(n)

Dasom = people_list.pop(0)
people_list.sort(reverse=True)
count = 0

while people_list and Dasom <= people_list[0]:
    Dasom += 1
    people_list[0] -= 1
    count += 1
    people_list.sort(reverse=True)

print(count)
