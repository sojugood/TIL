W = input()

stack = []

for i in W:
    if i in ['(', '[']:
        stack.append(i)
    elif i == ')':
        temp = 0
        if not stack or stack[-1] is int:
            print(0)
            exit()
        while stack:
            top = stack.pop()
            if top == '(':
                if temp == 0:
                    stack.append(2)
                else:
                    stack.append(2 * temp)
                break
            elif top == '[':
                print(0)
                exit()
            else:
                temp += top
    elif i == ']':
        temp = 0
        if not stack or stack[-1] is int:
            print(0)
            exit()
        while stack:
            top = stack.pop()
            if top == '[':
                if temp == 0:
                    stack.append(3)
                else:
                    stack.append(3 * temp)
                break
            elif top == '(':
                print(0)
                exit()
            else:
                temp += top
    else:
        print(0)
        exit()

if '(' in stack or '[' in stack:
    print(0)
else:
    print(sum(stack))