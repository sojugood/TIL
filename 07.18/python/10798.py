''' 짧은 코드

arr = [''] * 15
for i in range(5):
    s = input()

    for j in range(len(s)):
        arr[j] += s[j]

print(''.join(arr))

'''

A = []

for temp in range(5):
    temp = list(input())
    A.append(temp)

output = []

for i in range(15):
    for j in range(5):
        if len(A[j])>i :
            out = A[j][i]
            output.append(out)

print(''.join(map(str, output)))