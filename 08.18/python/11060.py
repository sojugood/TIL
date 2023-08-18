from collections import deque
import sys

input = sys.stdin.readline

def bfs(start, end):
    Q = deque([(start, Ai[start], 0)])
    visited = [False] * N
    visited[start] = True

    while Q:
        n, j, cnt = Q.popleft()
        if n == end:
            return cnt
        for i in range(1, j + 1):
            next_pos = n + i
            if next_pos > end:
                break
            if not visited[next_pos] and Ai[next_pos] != 0:
                visited[next_pos] = True
                Q.append((next_pos, Ai[next_pos], cnt + 1))
                
    return -1

N = int(input())

Ai = list(map(int, input().split()))

S = 0
G = N - 1

print(bfs(S, G))
