T = int(input())

for i in range(T):
    n = list(input())
    sum = 0
    A = 0
    for j in n:
        if j == 'O':
            sum += 1
            A += sum
        else:
            sum = 0
            A += sum
    print(A)