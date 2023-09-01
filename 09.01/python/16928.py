import sys
input = sys.stdin.readline
from collections import deque

def bfs(start):
    q = deque([(start, 0)])
    board[start] = 1
    while q:
        num, cnt = q.popleft()
        if num == 100:
            return cnt
        for n in range(1, 7):
            if num + n <= 100:
                if plus_lst[num + n]:
                    next = plus_lst[num + n]
                    if not board[next]:
                        q.append((next, cnt + 1))
                        board[next] = 1
                elif minus_lst[num + n]:
                    next = minus_lst[num + n]
                    if not board[next]:
                        q.append((next, cnt + 1))
                        board[next] = 1
                else:
                    next = num + n
                    if not board[next]:
                        q.append((next, cnt + 1))
                        board[next] = 1

N, M = map(int, input().split())

board = [0] * 101

plus_lst = [0] * 101

minus_lst = [0] * 101

for _ in range(N):
    x, y = map(int, input().split())
    plus_lst[x] = y

for _ in range(M):
    u, v = map(int, input().split())
    minus_lst[u] = v

print(bfs(1))