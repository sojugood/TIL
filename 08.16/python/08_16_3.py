def f(i, N, s, target): # s : i - 1 원소까지 부분집합의 합
    global cnt
    cnt += 1
    if s == target:
        print(bit, s)
    elif i == N:
        return
    elif s > target:    # 백트래킹
        return
    else:
        bit[i] = 1  # 부분집합에 A[i] 포함
        f(i + 1, N, s + A[i], target)
        bit[i] = 0  # 부분집합에 A[i] 미포함
        f(i + 1, N, s, target)

N = 10
cnt = 0
A = [i for i in range(1, N + 1)]
bit = [0] * N
f(0, N, 0, 10)
print(cnt)