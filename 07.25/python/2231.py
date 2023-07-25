N = int(input())

result = 0

for i in range(1, N + 1):
    num = i + sum(int(j) for j in str(i))
    if num == N:
        result = i
        break

print(result)