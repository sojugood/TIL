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

'''
def double_range(start, end):
    while start < end:
        yield start
        start *= 2  # 현재의 값에 2를 곱합니다.
'''

def double_range_reverse(start, end):
    while start > end:
        yield start
        start /= 2

X_list = []

for i in double_range_reverse(64, 0):
    if X - i >= 0:
        X = X - i
        X_list.append(i)
    elif X <= 0:
        break

total = len(X_list)
print(total)
