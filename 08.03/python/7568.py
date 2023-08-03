N = int(input())

l_list = []
for _ in range(N):
    l = list(map(int, input().split()))
    l_list.append(l)

result_list = []
for i in range(len(l_list)):
    count = 1
    temp = l_list[i]
    l_list.remove(temp)
    for j in l_list:
        if temp[0] < j[0] and temp[1] < j[1]:
            count += 1
    result_list.append(count)
    l_list.insert(i, temp)

print(*result_list)