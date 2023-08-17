from collections import deque

N, K = map(int, input().split())

d = deque(range(1, N + 1))

result = []

while d:
    d.rotate(-(K - 1))
    temp = d.popleft()
    result.append(temp)

print("<"+', '.join(map(str, result))+">")