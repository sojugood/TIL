'''
64
32
16 16
8 8
4 4 
2 2
1 1
'''

X = int(input())

def double_range(start, end):
    while start < end:
        yield start
        start *= 2  # 현재의 값에 2를 곱합니다.

X_list = []

if X in double_range(1, 65):
    print('1')
else:
    if X % 2 != 0:
        for i in double_range(1, 65):
            X = X - i
            X_list.append(i)
            if X in double_range(1, 65):
                X_list.append(X)
                break
    else:
        for i in double_range(2, 65):
            X = X - i
            X_list.append(i)
            if X in list(str(double_range(2, 65))):
                X_list.append(X)
                break
    total = len(X_list)
    print(total)