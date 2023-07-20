N = int(input())
S = 1
dot = 4

for i in range(1, N+1):
    dot = (dot - S) * (dot - S)
    S = S * 4

print(dot)