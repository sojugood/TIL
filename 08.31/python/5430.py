from collections import deque
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    p = input().strip()
    n = int(input())
    a = input().strip()

    if n == 0:
        deq = []
    else:
        deq = deque(a[1:-1].split(','))
    
    err = 0
    rev = False
    for i in p:
        if i == 'R':
            rev = not rev
        else:
            if len(deq) == 0:
                err = 1
                print('error')
                break
            if not rev:
                deq.popleft()
            else:
                deq.pop()
    
    if not err:
        if rev:
            deq.reverse()
        print(f"[{','.join(deq)}]")