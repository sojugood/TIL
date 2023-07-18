N = int(input())

all_list = []
change_list = []

for i in range(N):
    F = input()
    a = list(F)
    all_list.append(a)

b = len(all_list)

for k in range(len(all_list[0])):
    if all(all_list[j][k] == all_list[0][k] for j in range(b)):
        change_list.append(all_list[0][k])
    else:
        change_list.append('?')

result = ''.join(change_list)
print(result)

''' 쉬운 코드
N = int(input())

arr = [input() for _ in range(N)]


ans = ''
for i in range(len(arr[0])):
    tmp = arr[0][i]
    for j in arr[1:]:
        if j[i] != tmp:
            ans += '?'
            break
    else: ans += tmp
    
print(ans)
'''