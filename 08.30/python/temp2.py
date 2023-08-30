from collections import deque

N = int(input())

q = deque([])

for _ in range(N):
    x = int(input())
    if x != 0:
        q.append(x)
    else:
        if q:
            q = deque(sorted(q))
            tmp = q.popleft()
            while True:
                v = q.popleft()
                if v != tmp:
                    q.appendleft(v)
                    break
            print(tmp)
        else:
            print(0)
