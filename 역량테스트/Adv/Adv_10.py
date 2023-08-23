from collections import deque

def f(lst):
    result = 0
    q = deque(lst)
    for _ in range(N):
        for k in range(2, N - 5):
            i = 0
            j = 2
            r = N - 5 - k + 2
            while True:
                for m in range(2, r):
                    res = (q[i] + q[k])**2 + (q[i - j + N] + q[i - j + N - m])**2
                    result = max(result, res)
                j += 1
                r -= 1
                if j == N - 5:
                    break
        temp = q.popleft()
        q.append(temp)
    return result

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    print(f"#{tc} {f(lst)}")

