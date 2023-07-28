import sys
input = sys.stdin.readline

N = int(input())

h_list = []

for i in range(N):
    h = int(input())
    h_list.append(h)

def find_numbers(lst):
    stack = []
    for num in reversed(lst):
        if not stack or num > stack[-1]:
            stack.append(num)
    return stack[::-1]

result = len(find_numbers(h_list))

print(result)