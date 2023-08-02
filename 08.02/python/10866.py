import sys
input = sys.stdin.readline

N = int(input())

deque = []
for _ in range(N):
    command = input().split()
    if command[0] == 'push_front':
        X = command[-1]
        deque = [X] + deque
    elif command[0] == 'push_back':
        X = command[-1]
        deque.append(X)
    elif command[0] == 'pop_front':
        if len(deque) >= 1:
            result = deque[0]
            print(result)
            deque = deque[1:]
        else:
            print(-1)
    elif command[0] == 'pop_back':
        if len(deque) >= 1:
            result = deque.pop()
            print(result)
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(deque))
    elif command[0] == 'empty':
        if len(deque) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(deque) >= 1 and command[0] == 'front':
            print(deque[0])
        elif len(deque) >= 1 and command[0] == 'back':
            print(deque[-1])
        else:
            print(-1)