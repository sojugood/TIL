'''
3
1 2 3
4 5 6
7 8 9
'''

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

max_v = 0   # 모든 원소가 0 이상일 때,
for i in range(N):  # 모든 원소 arr[i][j]에 대해
    for j in range(N):
        # arr[i][j] 중심으로
        s = arr[i][j]
        for k in range(4):
            for p in range(1, m): # 십자가 크기 커질 때,(기본값 m = 2)
                ni, nj = i + di[k]*p, j + dj[k]*p
                if 0 <= ni < N and 0 <= nj < N: # 배열을 벗어나지 않으면
                    s += arr[ni][nj]
        # 여기까지 주변 원소를 포함한 합
        if max_v < s:
            max_v = s
print(max_v)