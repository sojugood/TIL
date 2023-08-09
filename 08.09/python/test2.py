X = int(input())
N = int(input())
temp = 0
for _ in range(N):
    a, b = map(int, input().split())
    temp += a*b
print('Yes' if temp == X else 'No')
