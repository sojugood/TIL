find_list = []
find_dict = {}

for i in range(1, 10):
    n = int(input())
    find_list.append(n)
    find_dict[n] = i

find_list.sort()

R = find_list[8]

print(R)
print(find_dict[R])