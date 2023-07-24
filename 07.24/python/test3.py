# main.py

# 아래 함수를 수정하시오.
def find_min_max(n):
    min_max_list = []
    n.sort()
    min_max_list.append(n[0])
    n.sort(reverse=True)
    min_max_list.append(n[0])
    return tuple(min_max_list)

result = find_min_max([3, 1, 7, 2, 5])
print(result) # (1, 7)
