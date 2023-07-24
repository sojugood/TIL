N = int(input())

n = map(int, input().split())

count = 0

for i in n:
    if i < 2:
        a = 0
    elif i == 2 or i == 3:
        a = 1
        count += a
    else:
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                a = 0
                break
            else:
                a = 1
        count += a

print(count)

'''
N = int(input())

num = map(int, input().split())

count = 0

for i in num:
    for j in range(2, i + 1):
        if i % j == 0:
            if i == j:
                count += 1
            break
            
print(count)
'''