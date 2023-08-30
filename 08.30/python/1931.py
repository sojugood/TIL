import sys
input = sys.stdin.readline

N = int(input())

lst = []

for _ in range(N):
    s, e = map(int, input().split())
    lst.append((s, e))

lst.sort(key=lambda x: (x[1], x[0]))

result = 0
now = 0

for s, e in lst:
    if now <= s:
        now = e
        result += 1

print(result)