'''
두 자연수 a b

(n // 4) + 1 = X 위치
n % 4 = Y 위치(결과값이 0 이면 4임)

ex)
a = 11
X 위치 : (11 // 4) + 1 = 3
Y 위치 : 11 % 4 = 3

b = 33
X 위치 : (33 // 4) + 1 = 9
Y 위치 : 33 % 4 = 1

X 거리 : 9 - 3 = 6
Y 거리 : |1 - 3| = 2
최단거리 : X 거리 + Y 거리 = 6 + 2 = 8
'''

A, B = map(int, input().split())

def X_location(n):
    locationX = (n // 4) + 1
    if (n % 4) == 0:
        return (n // 4)
    else:
        return locationX

def Y_location(n):
    locationY = (n % 4)
    if n >= 4 and n % 4 == 0:
        return 4
    else:
        return locationY

min_location_X = abs(X_location(B) - X_location(A))
min_location_Y = abs(Y_location(B) - Y_location(A))

min_location_result = min_location_X + min_location_Y

print(min_location_result)