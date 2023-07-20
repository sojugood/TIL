n = int(input())

total_S = n * 100

x_list = []
y_list = []

for i in range(n):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)

S_list = []
S_same_list = []

for j in range(n):
    for k in range(n):
        if j != k:  # Check if indexes are different
            if abs(y_list[j] - y_list[k]) < 10 and abs(x_list[j] - x_list[k]) < 10:
                S = (10 - abs(x_list[j] - x_list[k])) * (10 - abs(y_list[j] - y_list[k]))
                S_list.append(S)
            elif x_list[j] == x_list[k] and y_list[j] == y_list[k]:
                S = 100
                S_same_list.append(S)

S_sum = sum(S_list)
S_same_sum = sum(S_same_list)
result = total_S - S_sum - S_same_sum
print(result)
