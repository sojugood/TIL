import sys
input = sys.stdin.readline

def cal(A, B, C):
    cnt = 0
    for i in range(4):
        if A[i] != B[i]:
            cnt += 1
        if A[i] != C[i]:
            cnt += 1
        if B[i] != C[i]:
            cnt += 1
    return cnt

T = int(input())

for _ in range(T):
    N = int(input())
    mbti = list(input().split())
    
    if N > 34:
        print(0)
        continue

    result = float("inf")

    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                result = min(result, cal(mbti[i], mbti[j], mbti[k]))
    print(result)