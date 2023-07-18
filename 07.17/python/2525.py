A, B = map(int, input().split())
C = int(input())

if B + C >= 60:
    T = (B + C) // 60
    A1 = A + T
    if A1 >= 24:
        A1 = A1 - 24
    B1 = (B + C) % 60
elif B + C < 60:
    A1 = A
    B1 = B + C

print(A1, B1)