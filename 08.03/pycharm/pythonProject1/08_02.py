N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
# (0, 0) 기준 대각선 합
total1 = 0
for i in range(N):
    total1 += arr[i][i]

# (0, N) 기준 대각선 합
# total2 = 0
# total2 += arr[i][N - 1 - i]

'''
지그재그 순회

for i in range(n):
	for j in range(m):
		f(Array[i][j + (m-1 - 2*j) * (i%2)])

[j + (m-1 - 2*j) * (i%2)] <- i가 홀수일 때 m-1 - j 가 필요한데, 짝수일 때 j도 필요하므로 m-1 - j를 m-1 - 2j + j로 바꿔준다.


전치 행렬

for i in range(3):
	for j in range(3):
		if i < j:	# 조건이 있어야 한 번만 바꿈(두 번 바꾸면 제자리임)
			arr[i][j], arr[j][j] = arr[j][j], arr[i][j]
'''