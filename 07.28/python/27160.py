N = int(input())

STRAWBERRY = 0
BANANA = 0
LIME = 0
PLUM = 0

for i in range(N):
    S, X = input().split()
    if S == 'STRAWBERRY':
        STRAWBERRY += int(X)
    elif S == 'BANANA':
        BANANA += int(X)
    elif S == 'LIME':
        LIME += int(X)
    elif S == 'PLUM':
        PLUM += int(X)

if STRAWBERRY == 5 or BANANA == 5 or LIME == 5 or PLUM == 5:
    print('YES')
else:
    print('NO')