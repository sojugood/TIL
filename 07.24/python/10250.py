T = int(input())

for i in range(T):
    H, W, N = map(int, input().split())
    X = (N // H) + 1
    Y = N % H
    if Y == 0:
        Y = H
        X = (N // H)
    if X < 10:
        print(f"{Y}0{X}")
    else:
        print(f"{Y}{X}")