import sys
input = sys.stdin.readline

n = int(input())

number = 1

stack = []

result = []

for _ in range(n):
    nums = int(input())

    while number <= nums:
        stack.append(number)
        number += 1
        result.append('+')

    if stack[-1] == nums:
        stack.pop()
        result.append('-')

    else:
        result = ['NO']
        break

for i in result:
    print(i)