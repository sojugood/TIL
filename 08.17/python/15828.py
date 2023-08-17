from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

Q = deque()

while True:
    info = int(input())
    if info > 0:
        if len(Q) < N:
            Q.append(info)
    elif info == 0:
        Q.popleft()
    else:
        break

if Q:
    print(*Q)
else:
    print("empty")