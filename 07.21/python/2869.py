A, B, V = map(int, input().split())

if A == V:
    D = 1
elif V - A <= A - B:
    D = 2
elif ((V - A) % (A -B)) != 0:
    D = ((V - A) // (A - B)) + 2
else:
    D = ((V - A) // (A - B)) + 1

print(D)