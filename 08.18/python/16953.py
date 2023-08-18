from collections import deque

def bfs(num, target):
    Q = deque([(num, 1)])
    while Q:
        n, depth = Q.popleft()
        for i in lst:
            temp = n
            if i == 1:
                temp = temp * 2
                if temp == target:
                    return depth + 1
                elif temp > target:
                    continue
                Q.append((temp, depth + 1))
            else:
                temp = (temp * 10) + 1
                if temp == target:
                    return depth + 1
                elif temp > target:
                    continue
                Q.append((temp, depth + 1))
    return -1

A, B = map(int, input().split())
lst = [1, 2]
print(bfs(A, B))