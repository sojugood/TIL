from collections import deque
import sys
input = sys.stdin.readline

def bfs(start, target):
    q = deque([(start, 0)])
    visited = set([start])
    
    while q:
        current, cnt = q.popleft()
        
        if current == target:
            return cnt
        
        for next in [current - 1, current + 1, current * 2]:
            if next < 0 or next > 100000:
                continue
            if next not in visited:
                visited.add(next)
                q.append((next, cnt + 1))

N, K = map(int, input().split())
print(bfs(N, K))
