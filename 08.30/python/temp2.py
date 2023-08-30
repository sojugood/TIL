from collections import deque
import math

n = int(input())
queue = deque([(n, 0)])

visited = set()

while queue:
    value, steps = queue.popleft()

    if value == 0:
        print(steps)
        break

    for i in range(1, int(math.sqrt(value)) + 1):
        next_value = value - i*i
        if next_value >= 0 and next_value not in visited:
            queue.append((next_value, steps + 1))
            visited.add(next_value)
