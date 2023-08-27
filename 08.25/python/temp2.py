arr=[]
arr_cnt=[0]*26
n=input()
for i in range(97,123,1):
    arr.append(i)

for i in n:
    for j in range(26):
        if ord(i) == arr[j]:
            arr_cnt[j] += 1
        else : arr_cnt[j] += 0
print(*arr_cnt)