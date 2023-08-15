N = int(input())

Pi = list(map(int, input().split()))

Pi.sort()

cnt = len(Pi)

result = 0

for i in Pi:
    result += i * cnt
    cnt -= 1

print(result)