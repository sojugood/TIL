def f(i, N):
    if i == N:
        s = 0
        for j in range(N):
            if bit[j]:
                s += A[j]
                print(A[j], end =' ')
        print(f' : {s}')
        return
    else:
        bit[i] = 1
        f(i + 1, N)
        bit[i] = 0
        f(i + 1, N)

N = 3
A = [1, 2, 3]
bit = [0] * N
f(0, N)