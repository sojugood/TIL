W = input()

stack = []

temp = 1

result = 0

for i in range(len(W)):
    if W[i] == '(':
        temp *= 2
        stack.append(W[i])
    
    elif W[i] == '[':
        temp *= 3
        stack.append(W[i])

    elif W[i] == ')':
        if not stack or stack[-1] != '(':
            result = 0
            break
        if W[i - 1] == '(':
            result += temp
        temp //= 2
        stack.pop()
    
    elif W[i] == ']':
        if not stack or stack[-1] != '[':
            result = 0
            break
        if W[i - 1] == '[':
            result += temp
        temp //= 3
        stack.pop()

if stack:
    print(0)
else:
    print(result)