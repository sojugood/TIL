import sys
input = sys.stdin.readline

N = int(input())

queue = []
for _ in range(N):
    command = input().split()
    if command[0] == 'pop':
        if len(queue) >= 1:
            result = queue.pop()
            print(result)
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(queue))
    elif command[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'front':
        if len(queue) >= 1:
            print(queue[-1])
        else:
            print(-1)
    elif command[0] == 'back':
        if len(queue) >= 1:
            print(queue[0])
        else:
            print(-1)
    else:
        X = command[-1]
        queue = [X] + queue