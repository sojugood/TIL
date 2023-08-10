E = input()
stack = []
count = 0
temp = 0
for i in E:
    if i == '(':
        temp += 1
        stack += i
    elif i == ')':
        if stack[-1] == '(':
            temp -= 1
            count += temp
            stack += i
        else:
            count += 1
            temp -= 1
            stack += i
print(count)