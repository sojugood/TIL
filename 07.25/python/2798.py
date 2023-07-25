N, M = map(int, input().split())

card = set(map(int, input().split()))

sum_list = []

for i in card:
    for j in card:
        for k in card:
            nums = i + j + k
            if i != j and j != k and i != k and nums <= M:
                sum_list.append(nums)

sum_list.sort(reverse=True)

print(sum_list[0])