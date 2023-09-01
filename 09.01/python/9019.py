import sys
input = sys.stdin.readline
from collections import deque

def bfs(start, target):
    lst = ''
    visited = [-1] * 10000
    q = deque([(start, lst)])
    visited[start] = 0

    while q:
        num, temp = q.popleft()
        if num == target:
            return temp

        # D
        next_num = (num * 2) % 10000
        if visited[next_num] == -1:
            q.append((next_num, temp + 'D'))
            visited[next_num] = 0

        # S
        next_num = (num - 1) if num != 0 else 9999
        if visited[next_num] == -1:
            q.append((next_num, temp + 'S'))
            visited[next_num] = 0

        # L
        next_num = (num % 1000) * 10 + num // 1000
        if visited[next_num] == -1:
            q.append((next_num, temp + 'L'))
            visited[next_num] = 0

        # R
        next_num = (num % 10) * 1000 + num // 10
        if visited[next_num] == -1:
            q.append((next_num, temp + 'R'))
            visited[next_num] = 0

T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    print(bfs(A, B))
