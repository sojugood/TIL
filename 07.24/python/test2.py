N = int(input())

nums = set(input().split())

M = int(input())

nums_2 = input().split()

equal_list = []

result_list = []

for i in nums_2:
    if i in nums:
        equal_list.append(i)
    if bool(equal_list) == True:
        result_list.append(1)
        equal_list = []
    else:
        result_list.append(0)
        equal_list = []

print(*result_list)