F = input()
a = list(F)

b = len(a)
print(b)

for j in range(b):
    for k in range(b):
        if all_list[j][k]

for k in range(len(all_list[0])):
    if all(all_list[j][k] == all_list[0][k] for j in range(b)):
        change_list.append(all_list[0][k])
    else:
        change_list.append('?')

change_list_list = [str(i) for i in change_list]
change_str = ''.join(change_list_list)
result = int(change_str)