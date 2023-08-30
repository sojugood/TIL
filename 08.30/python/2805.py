import sys
input = sys.stdin.readline

N, M = map(int, input().split())

lst = list(map(int, input().split()))

start = 0
end = max(lst)
result = 0

while start <= end:
    target = (start + end) // 2
    temp = 0
    for i in lst:
        if i > target:
            temp += (i - target)
    if temp >= M:
        result = target
        start = target + 1
    else:
        end = target - 1

print(result)