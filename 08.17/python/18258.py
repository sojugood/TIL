from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

Q = deque()

for _ in range(N):
    command = list(input().split())
    if command[0] == 'push':
        Q.append(command[-1])
    elif command[0] == 'pop':
        if Q:
            print(Q.popleft())
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(Q))
    elif command[0] == 'empty':
        if Q:
            print(0)
        else:
            print(1)
    elif command[0] == 'front':
        if Q:
            temp = Q.popleft()
            print(temp)
            Q.appendleft(temp)
        else:
            print(-1)
    elif command[0] == 'back':
        if Q:
            temp = Q.pop()
            print(temp)
            Q.append(temp)
        else:
            print(-1)