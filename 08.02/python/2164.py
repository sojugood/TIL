from collections import deque

N = int(input())
card = deque(range(1, N + 1))

while len(card) > 1:
    card.popleft() # 왼쪽에서 제거
    card.append(card.popleft()) # 왼쪽에서 뽑아서 오른쪽에 추가

print(card[0])
