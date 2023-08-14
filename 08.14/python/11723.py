import sys
input = sys.stdin.readline
M = int(input())
S = set()
for _ in range(M):
    act = input().split()
    if act[0] == 'add':
        S.add(int(act[-1]))
    elif act[0] == 'remove':
        S.discard(int(act[-1]))
    elif act[0] == 'check':
        if int(act[-1]) in S:
            print(1)
        else:
            print(0)
    elif act[0] == 'toggle':
        if int(act[-1]) in S:
            S.remove(int(act[-1]))
        else:
            S.add(int(act[-1]))
    elif act[0] == 'all':
        S = set(range(1, 21))
    elif act[0] == 'empty':
        S = set()