A = []
list_max = []
M = []

for temp in range(9):
    temp = list(map(int,input().split()))
    max_value = max(temp)
    index = temp.index(max_value)
    M.append(index)
    list_max.append(max_value)
    A.append(temp)

list_max_value = max(list_max)
max_index = list_max.index(list_max_value)
value = M[max_index]
print(list_max_value)
print(max_index + 1, value + 1)