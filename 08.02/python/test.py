from collections import deque
import sys
input = sys.stdin.readline
N = int(input())

card = list(range(1, N + 1))
q = deque(card)

while len(card) > 1:
    q.popleft()
    temp = q.popleft()
    card.append(temp)