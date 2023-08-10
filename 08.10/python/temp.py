N = int(input())

count = 0

for _ in range(N):
    word = input()
    stack = []
    temp = 0
    for i in word:
        if not stack:
            stack += i
        else:
            if stack[-1] == i:
                temp = 1
                stack.pop()
            else:
                stack += i
    if stack:
        temp = 0
    count += temp
print(count)