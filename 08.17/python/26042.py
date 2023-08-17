import sys
input = sys.stdin.readline

n = int(input())

A = [list(map(int, input().split())) for _ in range(n)]

Q = []

lst = []

max_len = 0

for i in range(n):
    if A[i][0] == 1:
        Q.append(A[i][-1])
    else:
        if len(Q) > max_len:
            lst.append(Q[:])
            max_len = len(Q)
        elif len(Q) == max_len and Q[-1] < lst[-1][-1]:
            lst.append(Q[:])
        Q.pop(0)
if len(Q) > max_len:
    lst.append(Q[:])
    max_len = len(Q)
elif len(Q) == max_len and Q[-1] < lst[-1][-1]:
    lst.append(Q[:])
    
print(max_len, lst[-1][-1])