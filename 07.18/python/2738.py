N, M = map(int, input().split())

matrix_1 = []
matrix_2 = []

for i in range(N):
    row_1 = list(map(int, input().split()))
    matrix_1.append(row_1)

for j in range(N):
    row_2 = list(map(int, input().split()))
    matrix_2.append(row_2)

result = []

for k in range(len(matrix_1)):
    temp_row = [] # 각 행에 대한 결과를 저장할 임시 리스트
    for l in range(len(matrix_1[0])):
        matrix = matrix_1[k][l] + matrix_2[k][l]
        temp_row.append(matrix) # 각 요소를 임시 리스트에 추가
    result.append(temp_row) # 각 행의 결과를 result에 추가

for row in result:
    print(' '.join(map(str, row)))

''' 행렬 덧셈

n, m = map(int, input().split())

A, B = [], []

for temp in range(n):
    temp = list(map(int,input().split()))
    A.append(temp)

for temp in range(n):
    temp = list(map(int,input().split()))
    B.append(temp)
    
for i in range(n):
    for j in range(m):
        print(A[i][j]+B[i][j],end=' ')
    print()

'''