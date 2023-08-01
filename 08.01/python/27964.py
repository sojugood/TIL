n = int(input())

arr = list(map(str, input().split()))

arr_set = set(arr)

count = 0

for i in arr_set:
    if i[-6:] == 'Cheese':
        count += 1

if count >= 4:
    print('yummy')
else:
    print('sad')