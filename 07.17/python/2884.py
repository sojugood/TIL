H, M = map(int, input().split())

if M >= 45:
    H1 = H
    M1 = M - 45
elif M < 45:
    H1 = H - 1
    if H1 == (-1):
        H1 = 23
    M1 = M + 15

print(H1, M1)