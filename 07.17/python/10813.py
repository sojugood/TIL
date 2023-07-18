M, N = map(int, input().split())

Jul = list(range(1, M + 1))

for _ in range(N):
    X, Y = list(map(int, input().split()))
    X, Y = X - 1, Y - 1
    Jul[X], Jul[Y] = Jul[Y], Jul[X]

result = ' '.join(map(str, Jul))
print(result)