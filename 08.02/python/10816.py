from bisect import bisect_left, bisect_right

def count_by_range(arr, left_value, right_value):
    right_index = bisect_right(arr, right_value)
    left_index = bisect_left(arr, left_value)
    return right_index - left_index

N = int(input())
list1 = list(map(int, input().split()))
M = int(input())
list2 = list(map(int, input().split()))

list1.sort() # 리스트1 정렬

result_list = []
for num in list2:
    count = count_by_range(list1, num, num)
    result_list.append(count)

print(*result_list)

'''
# 1
from collections import Counter

N = int(input())
list1 = list(map(int, input().split()))
M = int(input())
list2 = list(map(int, input().split()))

counter = Counter(list1)
result_list = []
for num in list2:
    count = counter[num]
    result_list.append(count)
    
print(*result_list)

# 2
N = int(input())
aL1 = list(map(int, input().split()))
M = int(input())
bL = list(map(int, input().split()))

count_dict = {}
for num in aL1:
    count_dict[num] = count_dict.get(num, 0) + 1

for num in bL:
    print(count_dict.get(num, 0))
'''