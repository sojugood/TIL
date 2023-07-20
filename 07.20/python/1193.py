X = int(input())

s = 0
for i in range(1, X + 1):
    s += i
    if X <= s:
        if i % 2 != 0:
            print(f"{1 + (s - X)}/{i - (s - X)}")
            break
        else:
            print(f"{i - (s - X)}/{1 + (s - X)}")
            break