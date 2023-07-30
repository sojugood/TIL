N = int(input())

number_list = list(range(1, N + 1))
result_list = []

for i in range(N):
    result = number_list.pop(0)
    result_list.append(result)
    if i == N - 1:
        break
    else:
        move = number_list.pop(0)
        number_list.append(move)

print(*result_list)